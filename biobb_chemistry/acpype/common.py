""" Common functions for package biobb_chemistry.acpype """
import shlex
import shutil
from pathlib import Path
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools import file_utils as fu


# acpype options available as properties: property name -> (acpype flag, acpype default)
ACPYPE_OPTIONS = {
    "charge": ("-n", None),
    "charge_method": ("-c", "bcc"),
    "multiplicity": ("-m", 1),
    "atom_type": ("-a", "gaff2"),
    "protein_ff": ("-F", "ff14SB"),
    "qprog": ("-q", "sqm"),
    "keyword": ("-k", None),
    "max_time": ("-s", 10800),
    "predindex": ("-r", 4),
    "gmx4": ("-z", False),
    "merge": ("-g", False),
    "sorted": ("-l", False),
    "cnstop": ("-t", False),
    "chiral": ("-j", False),
    "split_molecules": ("-S", False),
    "direct": ("-u", False),
}

# Accepted values of the options with a closed list of values
ACPYPE_CHOICES = {
    "charge_method": ["gas", "bcc", "abcg2", "user"],
    "atom_type": ["gaff", "amber", "gaff2", "amber2"],
    "protein_ff": ["ff14SB", "ff99SB"],
    "qprog": ["mopac", "sqm", "divcon"],
    "predindex": [0, 1, 2, 3, 4, 5],
}

# Options that acpype 2023.10.27 (the oldest supported version) does not have:
# they are only written to the command line when they are not the default value
ACPYPE_NEW_OPTIONS = {"protein_ff", "predindex", "split_molecules"}

# Options of the blocks that parameterize a molecule (-i input)
PARAMS_OPTIONS = ["charge", "charge_method", "multiplicity", "atom_type", "protein_ff", "qprog", "keyword", "max_time", "predindex"]
# Options of the GROMACS topologies
GMX_OPTIONS = ["gmx4", "merge", "sorted"]
# Options of the CNS topologies
CNS_OPTIONS = ["cnstop", "chiral"]
# Options of the AMBER to GROMACS conversion (-x inpcrd -p prmtop)
AMB2GMX_OPTIONS = GMX_OPTIONS + ["split_molecules", "direct"]


class AcpypeBase(BiobbObject):
    """Base class of the acpype blocks: goes from the properties to the acpype command, run in the
    sandbox, and from the files acpype writes to the outputs."""

    #: Input arguments -> acpype flag
    acpype_inputs: dict[str, str] = {"input_path": "-i"}
    #: Properties of the block that are acpype options, see ACPYPE_OPTIONS
    acpype_options: list[str] = []
    #: Output arguments -> file acpype writes, after the basename (ie: "_GMX.gro" for BBB_GMX.gro)
    acpype_outputs: dict[str, str] = {}
    #: Files included by an output (#include of a GROMACS top, @ of a CNS inp), renamed to the
    #: name of the output: {output argument: {file acpype includes, after the basename: output argument}}
    acpype_includes: dict[str, dict[str, str]] = {}
    #: Folder acpype writes, after the basename
    acpype_folder = ".acpype"

    def prepare(self) -> None:
        """Checks the basename, the charge and the values of the acpype options"""
        if not self.basename:
            fu.log('No basename provided, default value BBB assigned', self.out_log)
        self.basename = str(self.basename or 'BBB')

        if "charge" in self.acpype_options:
            if self.charge is None or self.charge == '':
                fu.log('Charge will be guessed by acpype.', self.out_log)
                self.charge = None
            elif not isinstance(self.charge, int):
                fu.log('Value %s is not compatible as a charge value, default value 0 assigned' % self.charge, self.out_log)
                self.charge = 0

        classname = type(self).__name__
        for name in self.acpype_options:
            value = getattr(self, name)
            if name in ACPYPE_CHOICES and value not in ACPYPE_CHOICES[name]:
                fu.log(classname + ': Value %s of the %s property is not valid, accepted values: %s' % (value, name, ', '.join(map(str, ACPYPE_CHOICES[name]))), self.out_log)
                raise SystemExit(classname + ': Value %s of the %s property is not valid' % (value, name))

    def run(self) -> None:
        """Runs acpype in the sandbox and copies the files it writes to the outputs"""
        self.cmd = [self.binary_path]
        self.cmd += [flag + ' ' + self.stage_io_dict["in"][arg] for arg, flag in self.acpype_inputs.items()]
        self.cmd.append('-b ' + self.basename)
        for name in self.acpype_options:
            flag, default = ACPYPE_OPTIONS[name]
            value = getattr(self, name)
            if isinstance(default, bool):
                if value:
                    self.cmd.append(flag)
            elif value is None or value == '' or (name in ACPYPE_NEW_OPTIONS and value == default):
                continue
            elif name == "keyword":
                self.cmd.append(flag + ' ' + shlex.quote(str(value)))
            else:
                self.cmd.append(flag + ' ' + str(value))

        self.run_biobb()

        # acpype writes its folder where it runs: in the sandbox
        folder = Path(self.stage_io_dict["unique_dir"]) / (self.basename + self.acpype_folder)
        for arg, suffix in self.acpype_outputs.items():
            src = folder / (self.basename + suffix)
            if src.is_file():
                shutil.copy(src, self.sandbox_file(arg))
                fu.log('File %s created' % self.io_dict["out"][arg], self.out_log)

        for arg, includes in self.acpype_includes.items():
            output = Path(self.sandbox_file(arg))
            if output.is_file():
                text = output.read_text()
                for suffix, included in includes.items():
                    text = text.replace(self.basename + suffix, Path(self.sandbox_file(included)).name)
                output.write_text(text)
