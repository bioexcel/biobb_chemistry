"""Common functions for package biobb_chemistry.babel"""

import re
from pathlib import Path, PurePath

from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools import file_utils as fu


class BabelBase(BiobbObject):
    """Base class of the obabel blocks: goes from the properties to the obabel command, and removes
    from a PDBQT output the records Open Babel copies from the input."""

    def prepare(self) -> None:
        """Checks the formats, the coordinates and the pH"""
        self.fs_input = fu.str_to_list(self.fs_input)
        self.fs_output = fu.str_to_list(self.fs_output)
        self.input_format = get_input_format(self.input_format, self.io_dict["in"]["input_path"], self.out_log)
        self.output_format = get_output_format(self.output_format, self.io_dict["out"]["output_path"], self.out_log)

        if self.coordinates is not None and str(self.coordinates) not in ("2", "3"):
            fu.log("Value %s is not compatible as a coordinates value" % self.coordinates, self.out_log)
            self.coordinates = None

        if self.ph == "":
            self.ph = None
        if self.ph is not None and not isinstance(self.ph, (int, float)):
            fu.log("Incorrect format for pH, no value assigned", self.out_log)
            self.ph = None

    def obabel_flags(self) -> list[str]:
        """Goes from the properties of the block to its own obabel flags, written after the coordinates"""
        return []

    def run(self) -> None:
        """Runs obabel and removes the input PDB records that Open Babel >= 3.2 copies to a PDBQT output"""
        self.cmd = [self.binary_path,
                    "-i" + self.input_format, self.stage_io_dict["in"]["input_path"],
                    "-o" + self.output_format, "-O" + self.stage_io_dict["out"]["output_path"]]
        if self.coordinates is not None:
            self.cmd.append("--gen%sd" % self.coordinates)
        self.cmd += self.obabel_flags()
        self.cmd += ["-a" + fsi for fsi in self.fs_input or []]
        self.cmd += ["-x" + fso for fso in self.fs_output or []]
        # effort only for 3D coordinates
        if str(self.coordinates) == "3":
            self.cmd.append("--" + self.effort)

        self.run_biobb()

        remove_non_pdbqt_records(self.output_format, self.sandbox_file("output_path"), self.out_log)


def get_input_format(input_format, input_path, out_log):
    """Checks if provided input format is correct"""
    infr = input_format
    if not is_valid_input(infr):
        file_extension = PurePath(input_path).suffix
        if infr is not None:
            fu.log(
                "Format %s is not compatible as an input format, assigned input file extension: %s"
                % (infr, file_extension[1:]),
                out_log,
            )
        infr = file_extension[1:]

    return infr


def get_output_format(output_format, output_path, out_log):
    """Checks if provided output format is correct"""
    oufr = output_format
    if not is_valid_output(oufr):
        file_extension = PurePath(output_path).suffix
        if oufr is not None:
            fu.log(
                "Format %s is not compatible as an output format, assigned output file extension: %s"
                % (oufr, file_extension[1:]),
                out_log,
            )
        oufr = file_extension[1:]

    return oufr


# Records of the PDBQT format (AutoDock / Vina). Open Babel >= 3.2 also copies the
# PDB records of the input it does not use (HEADER, COMPND, AUTHOR, SEQRES...) to a
# PDBQT output, and Vina rejects them: "Unknown or inappropriate tag found".
PDBQT_RECORDS = ("ATOM", "HETATM", "REMARK", "ROOT", "ENDROOT", "BRANCH", "ENDBRANCH",
                 "TORSDOF", "BEGIN_RES", "END_RES", "MODEL", "ENDMDL", "TER", "END")


def remove_non_pdbqt_records(output_format, output_path, out_log):
    """Removes from a PDBQT output file the lines that are not PDBQT records"""
    if not is_valid_output(output_format):
        output_format = PurePath(output_path).suffix[1:]
    if output_format != "pdbqt" or not Path(output_path).exists():
        return

    lines = Path(output_path).read_text().splitlines(keepends=True)
    pdbqt_lines = [line for line in lines if not line.strip() or line.startswith(PDBQT_RECORDS)]
    if len(pdbqt_lines) < len(lines):
        Path(output_path).write_text("".join(pdbqt_lines))
        fu.log(
            "Removed %d non PDBQT records (copied from the input by Open Babel) from %s"
            % (len(lines) - len(pdbqt_lines), output_path),
            out_log,
        )


# obminimize options: property -> (flag, type or accepted values). The options not set or not
# valid are left out: obminimize uses its own default
MINIMIZE_OPTIONS = {
    "criteria": ("-c {}", float),
    "method": ("-{}", ["cg", "sd"]),
    "force_field": ("-ff {}", ["GAFF", "Ghemical", "MMFF94", "MMFF94s", "UFF"]),
    "hydrogens": ("-h", bool),
    "steps": ("-n {}", int),
    "cutoff": ("-cut", bool),
    "rvdw": ("-rvdw {}", float),
    "rele": ("-rele {}", float),
    "frequency": ("-pf {}", int),
}


def is_valid_minimize_value(value, kind) -> bool:
    """Goes from the value of an obminimize option and its type or accepted values to whether it is valid"""
    value = str(value)
    if isinstance(kind, list):
        return value in kind
    if kind is bool:
        return value in ("True", "False")
    if kind is int:
        return re.fullmatch(r"\d+", value) is not None
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_valid_input(ext):
    """Checks if input file format is compatible with Open Babel"""
    formats = [
        "dat",
        "ent",
        "fa",
        "fasta",
        "gro",
        "inp",
        "log",
        "mcif",
        "mdl",
        "mmcif",
        "mol",
        "mol2",
        "pdb",
        "pdbqt",
        "png",
        "sdf",
        "smi",
        "smiles",
        "txt",
        "xml",
        "xtc",
    ]
    return ext in formats


def is_valid_output(ext):
    """Checks if output file format is compatible with Open Babel"""
    formats = [
        "ent",
        "fa",
        "fasta",
        "gro",
        "inp",
        "mcif",
        "mdl",
        "mmcif",
        "mol",
        "mol2",
        "pdb",
        "pdbqt",
        "png",
        "sdf",
        "smi",
        "smiles",
        "txt",
    ]
    return ext in formats
