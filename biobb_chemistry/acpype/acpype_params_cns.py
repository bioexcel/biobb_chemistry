#!/usr/bin/env python3

"""Module containing the AcpypeParamsCNS class and the command line interface."""
from typing import Optional
from biobb_common.generic.biobb_object import BiobbObject
from biobb_chemistry.acpype.common import get_binary_path, get_basename, get_charge, create_unique_name, get_default_value, process_output_cns, get_acpype_options, get_acpype_options_cmd, CNS_OPTIONS, PARAMS_OPTIONS
import os


class AcpypeParamsCNS(BiobbObject):
    """
    | biobb_chemistry AcpypeParamsCNS
    | This class is a wrapper of `Acpype <https://github.com/alanwilter/acpype>`_ tool for small molecule parameterization for CNS/XPLOR MD package.
    | Generation of topologies for CNS/XPLOR. Acpype is a tool based in Python to use Antechamber to generate topologies for chemical compounds and to interface with others python applications like CCPN or ARIA. `Visit the official page <https://github.com/alanwilter/acpype>`_.

    Args:
        input_path (str): Path to the input file. File type: input. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/acpype/acpype.params.mol2>`_. Accepted formats: pdb (edam:format_1476), mdl (edam:format_3815), mol2 (edam:format_3816).
        output_path_par (str): Path to the PAR output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.cns.par>`_. Accepted formats: par (edam:format_3881).
        output_path_inp (str): Path to the INP output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.cns.inp>`_. Accepted formats: inp (edam:format_3878).
        output_path_top (str): Path to the TOP output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.cns.top>`_. Accepted formats: top (edam:format_3881).
        output_path_pdb (str): Path to the PDB output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.cns.pdb>`_. Accepted formats: pdb (edam:format_1476).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **basename** (*str*) - ("BBB") A basename for the project (folder and output files).
            * **charge** (*int*) - (0) [-20~20|1] Net molecular charge, for gas default is 0. If None the charge is guessed by acpype.
            * **charge_method** (*str*) - ("bcc") Charge method. Values: gas (Gasteiger charges), bcc (AM1-BCC charges), abcg2 (ABCG2 charges; recommended for GAFF2; not available in acpype 2023.10.27), user (charges read from the mol2 input file).
            * **multiplicity** (*int*) - (1) [1~10|1] Multiplicity (2S+1) of the molecule.
            * **atom_type** (*str*) - ("gaff2") Atom type. Values: gaff (General AMBER Force Field), amber (protein force field set in protein_ff + GAFF), gaff2 (General AMBER Force Field 2), amber2 (protein force field set in protein_ff + GAFF2).
            * **protein_ff** (*str*) - ("ff14SB") Protein force field used with the amber and amber2 atom types; only written to the command line when it is not the default value, not available in acpype 2023.10.27. Values: ff14SB (AMBER ff14SB), ff99SB (AMBER ff99SB).
            * **qprog** (*str*) - ("sqm") AM1-BCC charges engine; mopac and divcon need a full external AmberTools. Values: sqm (sqm), mopac (MOPAC), divcon (DivCon).
            * **keyword** (*str*) - (None) Keyword of the mopac or sqm engine, ie: "qm_theory='AM1', grms_tol=0.0005, scfconv=1.d-10".
            * **max_time** (*int*) - (10800) [1~1000000|1] Maximum time (in seconds) for the sqm or mopac execution.
            * **predindex** (*int*) - (4) [0~5|1] Antechamber atom and bond type prediction index, the antechamber -j flag; only 1, 4 and 5 produce a topology. Only written to the command line when it is not the default value, not available in acpype 2023.10.27. Values: 0 (no prediction), 1 (atom type), 2 (full bond types), 3 (part bond types), 4 (atom and full bond type), 5 (atom and part bond type).
            * **cnstop** (*bool*) - (False) Write the CNS topology with allhdg-like parameters (experimental).
            * **chiral** (*bool*) - (False) Create improper dihedral parameters for chiral atoms in CNS.
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

            from biobb_chemistry.acpype.acpype_params_cns import acpype_params_cns
            prop = {
                'basename': 'BBB',
                'charge': 0
            }
            acpype_params_cns(input_path='/path/to/myStructure.mol2',
                            output_path_par='/path/to/newPAR.par',
                            output_path_inp='/path/to/newINP.inp',
                            output_path_top='/path/to/newTOP.top',
                            output_path_top='/path/to/newPDB.pdb',
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

    def __init__(self, input_path, output_path_par, output_path_inp, output_path_top, output_path_pdb,
                 properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = {
            "in": {"input_path": input_path},
            "out": {"output_path_par": output_path_par, "output_path_inp": output_path_inp, "output_path_top": output_path_top, "output_path_pdb": output_path_pdb}
        }

        # Properties specific for BB
        self.basename = properties.get('basename', 'BBB')
        self.charge = properties.get('charge', '')
        self.binary_path = get_binary_path(properties, 'binary_path')
        self.acpype_options = PARAMS_OPTIONS + CNS_OPTIONS
        get_acpype_options(self, properties, self.acpype_options)
        self.properties = properties

        self.output_files = {
            'par': self.io_dict["out"]["output_path_par"],
            'inp': self.io_dict["out"]["output_path_inp"],
            'top': self.io_dict["out"]["output_path_top"],
            'pdb': self.io_dict["out"]["output_path_pdb"],
        }

    def create_cmd(self, container_io_dict, out_log, err_log):
        """Creates the command line instruction using the properties file settings"""
        instructions_list = []

        # generating output path
        if self.container_path:
            self.container_working_dir = self.container_volume_path
            out_pth = get_basename(self.basename, out_log) + '.' + self.unique_name
            instructions_list.append('cd ' + self.container_volume_path + ' &&')
        else:
            out_pth = get_basename(self.basename, out_log) + '.' + self.unique_name

        # executable path
        instructions_list.append(self.binary_path)

        # generating input
        ipath = '-i ' + container_io_dict["in"]["input_path"]
        instructions_list.append(ipath)

        # generating output
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

    def run(self) -> int:
        """Execute the :class:`AcpypeParamsCNS <acpype.acpype_params_cns.AcpypeParamsCNS>` acpype.acpype_params_cns.AcpypeParamsCNS object."""

        # create unique name for temporary folder (created by acpype)
        self.unique_name = create_unique_name(6)

        # create command line instruction
        self.cmd = self.create_cmd(self.stage_io_dict, self.out_log, self.err_log)

        # Run Biobb block
        self.run_biobb()

        # Copy files to host
        self.copy_to_host()

        # move files to output_path and removes temporary folder
        if self.container_path:
            process_output_cns(
                self.unique_name,
                os.path.join(self.stage_io_dict['unique_dir'], self.basename + "." + self.unique_name + ".acpype"),
                self.basename,
                get_default_value(self.__class__.__name__),
                self.output_files, self.out_log)
        else:
            self.tmp_files.append(self.basename + "." + self.unique_name + ".acpype")
            process_output_cns(
                self.unique_name,
                self.basename + "." + self.unique_name + ".acpype",
                self.basename,
                get_default_value(self.__class__.__name__),
                self.output_files, self.out_log)

        self.remove_tmp_files()
        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code


def acpype_params_cns(input_path: str, output_path_par: str, output_path_inp: str, output_path_top: str, output_path_pdb: str, properties: Optional[dict] = None, **kwargs) -> int:
    """Create the :class:`AcpypeParamsCNS <acpype.acpype_params_cns.AcpypeParamsCNS>` class and
    execute the :meth:`launch() <acpype.acpype_params_cns.AcpypeParamsCNS.launch>` method."""
    return AcpypeParamsCNS(**dict(locals())).launch()


acpype_params_cns.__doc__ = AcpypeParamsCNS.__doc__
main = AcpypeParamsCNS.get_main(acpype_params_cns, "Small molecule parameterization for CNS/XPLOR MD package.")

if __name__ == '__main__':
    main()
