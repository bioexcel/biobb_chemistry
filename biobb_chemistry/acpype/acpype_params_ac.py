#!/usr/bin/env python3

"""Module containing the AcpypeParamsAC class and the command line interface."""
from typing import Optional
from biobb_common.generic.biobb_object import BiobbObject
from biobb_chemistry.acpype.common import get_binary_path, get_basename, get_charge, create_unique_name, get_default_value, process_output, get_acpype_options, get_acpype_options_cmd, PARAMS_OPTIONS
import os


class AcpypeParamsAC(BiobbObject):
    """
    | biobb_chemistry AcpypeParamsAC
    | This class is a wrapper of `Acpype <https://github.com/alanwilter/acpype>`_ tool for small molecule parameterization for AMBER MD package.
    | Generation of topologies for Antechamber. Acpype is a tool based in Python to use Antechamber to generate topologies for chemical compounds and to interface with others python applications like CCPN or ARIA. `Visit the official page <https://github.com/alanwilter/acpype>`_.

    Args:
        input_path (str): Path to the input file. File type: input. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/acpype/acpype.params.mol2>`_. Accepted formats: pdb (edam:format_1476), mdl (edam:format_3815), mol2 (edam:format_3816).
        output_path_frcmod (str): Path to the FRCMOD output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.ac.frcmod>`_. Accepted formats: frcmod (edam:format_3888).
        output_path_inpcrd (str): Path to the INPCRD output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.ac.inpcrd>`_. Accepted formats: inpcrd (edam:format_3878).
        output_path_lib (str): Path to the LIB output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.ac.lib>`_. Accepted formats: lib (edam:format_3889).
        output_path_prmtop (str): Path to the PRMTOP output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.ac.prmtop>`_. Accepted formats: prmtop (edam:format_3881).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **basename** (*str*) - ("BBB") A basename for the project (folder and output files).
            * **charge** (*int*) - (None) [-20~20|1] Net molecular charge, for gas default is 0. If None the charge is guessed by acpype.
            * **charge_method** (*str*) - ("bcc") Charge method. Values: gas (Gasteiger charges), bcc (AM1-BCC charges), abcg2 (ABCG2 charges; recommended for GAFF2; not available in acpype 2023.10.27), user (charges read from the mol2 input file).
            * **multiplicity** (*int*) - (1) [1~10|1] Multiplicity (2S+1) of the molecule.
            * **atom_type** (*str*) - ("gaff2") Atom type. Values: gaff (General AMBER Force Field), amber (protein force field set in protein_ff + GAFF), gaff2 (General AMBER Force Field 2), amber2 (protein force field set in protein_ff + GAFF2).
            * **protein_ff** (*str*) - ("ff14SB") Protein force field used with the amber and amber2 atom types; only written to the command line when it is not the default value, not available in acpype 2023.10.27. Values: ff14SB (AMBER ff14SB), ff99SB (AMBER ff99SB).
            * **qprog** (*str*) - ("sqm") AM1-BCC charges engine; mopac and divcon need a full external AmberTools. Values: sqm (sqm), mopac (MOPAC), divcon (DivCon).
            * **keyword** (*str*) - (None) Keyword of the mopac or sqm engine, ie: "qm_theory='AM1', grms_tol=0.0005, scfconv=1.d-10".
            * **max_time** (*int*) - (10800) [1~1000000|1] Maximum time (in seconds) for the sqm or mopac execution.
            * **predindex** (*int*) - (4) [0~5|1] Antechamber atom and bond type prediction index, the antechamber -j flag; only 1, 4 and 5 produce a topology. Only written to the command line when it is not the default value, not available in acpype 2023.10.27. Values: 0 (no prediction), 1 (atom type), 2 (full bond types), 3 (part bond types), 4 (atom and full bond type), 5 (atom and part bond type).
            * **binary_path** (*str*) - ("acpype") Path to the acpype executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.
            * **container_path** (*str*) - (None) Container path definition.
            * **container_image** (*str*) - ('acpype/acpype:2022.7.21') Container image definition.
            * **container_volume_path** (*str*) - ('/tmp') Container volume path definition.
            * **container_working_dir** (*str*) - (None) Container working directory definition.
            * **container_user_id** (*str*) - (None) Container user_id definition.
            * **container_shell_path** (*str*) - ('/bin/bash') Path to default shell inside the container.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_chemistry.acpype.acpype_params_ac import acpype_params_ac
            prop = {
                'basename': 'BBB',
                'charge': 0
            }
            acpype_params_ac(input_path='/path/to/myStructure.mol2',
                            output_path_frcmod='/path/to/newFRCMOD.frcmod',
                            output_path_inpcrd='/path/to/newINPCRD.inpcrd',
                            output_path_lib='/path/to/newLIB.lib',
                            output_path_prmtop='/path/to/newPRMTOP.prmtop',
                            properties=prop)

    Info:
        * wrapped_software:
            * name: Acpype
            * version: 2019.10.05.12.26
            * license: GNU
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, input_path, output_path_frcmod, output_path_inpcrd, output_path_lib, output_path_prmtop,
                 properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = {
            "in": {"input_path": input_path},
            "out": {"output_path_frcmod": output_path_frcmod, "output_path_inpcrd": output_path_inpcrd, "output_path_lib": output_path_lib, "output_path_prmtop": output_path_prmtop}
        }

        # Properties specific for BB
        self.basename = properties.get('basename', 'BBB')
        self.charge = properties.get('charge', '')
        self.binary_path = get_binary_path(properties, 'binary_path')
        self.acpype_options = PARAMS_OPTIONS
        get_acpype_options(self, properties, self.acpype_options)
        self.properties = properties

        # Output files by extension, written by run() in the sandbox
        self.output_files = {
            'frcmod': "output_path_frcmod",
            'inpcrd': "output_path_inpcrd",
            'lib': "output_path_lib",
            'prmtop': "output_path_prmtop",
        }

    def create_cmd(self, container_io_dict, out_log, err_log):
        """Creates the command line instruction using the properties file settings"""
        instructions_list = []

        # generating output path
        self.basename = get_basename(self.basename, out_log)
        if self.container_path:
            # instructions_list.append('cd ' + self.container_volume_path + ';')
            # out_pth = self.container_volume_path + '/' + get_basename(self.basename, out_log) + '.' + self.unique_name
            self.container_working_dir = self.container_volume_path
            out_pth = self.basename + '.' + self.unique_name
            instructions_list.append('cd ' + self.container_volume_path + ' &&')
        else:
            out_pth = self.basename + '.' + self.unique_name

        # executable path
        instructions_list.append(self.binary_path)

        # generating input
        ipath = '-i ' + container_io_dict["in"]["input_path"]
        instructions_list.append(ipath)

        basename = '-b ' + out_pth
        instructions_list.append(basename)

        # adding charge if not none
        charge = get_charge(self.charge, out_log)
        if charge:
            charge = '-n ' + charge
            instructions_list.append(charge)

        # adding the acpype options
        instructions_list.extend(get_acpype_options_cmd(self, self.acpype_options, out_log, self.__class__.__name__))

        return instructions_list

    def run(self) -> None:
        """Execute the :class:`AcpypeParamsAC <acpype.acpype_params_ac.AcpypeParamsAC>` acpype.acpype_params_ac.AcpypeParamsAC object."""

        # create unique name for temporary folder (created by acpype)
        self.unique_name = create_unique_name(6)

        # create command line instruction
        self.cmd = self.create_cmd(self.stage_io_dict, self.out_log, self.err_log)

        # Run Biobb block
        self.run_biobb()

        # Copy the files that acpype writes in its folder to the output paths, with the original name in them.
        output_files = {extension: self.sandbox_file(file_ref) for extension, file_ref in self.output_files.items()}
        if self.container_path or self.chdir_sandbox:
            process_output(self.unique_name,
                           os.path.join(self.stage_io_dict['unique_dir'], self.basename + "." + self.unique_name + ".acpype"),
                           self.basename,
                           get_default_value(self.__class__.__name__),
                           output_files, self.out_log)
        else:
            self.tmp_files.append(self.basename + "." + self.unique_name + ".acpype")
            process_output(self.unique_name,
                           self.basename + "." + self.unique_name + ".acpype",
                           self.basename,
                           get_default_value(self.__class__.__name__),
                           output_files, self.out_log)


def acpype_params_ac(input_path: str, output_path_frcmod: str, output_path_inpcrd: str, output_path_lib: str, output_path_prmtop: str, properties: Optional[dict] = None, **kwargs) -> int:
    """Create the :class:`AcpypeParamsAC <acpype.acpype_params_ac.AcpypeParamsAC>` class and
    execute the :meth:`launch() <acpype.acpype_params_ac.AcpypeParamsAC.launch>` method."""
    return AcpypeParamsAC(**dict(locals())).launch()


acpype_params_ac.__doc__ = AcpypeParamsAC.__doc__
main = AcpypeParamsAC.get_main(acpype_params_ac, "Small molecule parameterization for AMBER MD package.")

if __name__ == '__main__':
    main()
