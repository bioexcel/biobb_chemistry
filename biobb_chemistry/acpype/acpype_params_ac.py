#!/usr/bin/env python3

"""Module containing the AcpypeParamsAC class and the command line interface."""
import argparse
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import  settings
from biobb_common.tools.file_utils import launchlogger
from biobb_chemistry.acpype.common import *


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
            * **charge** (*int*) - (0) [-20~20|1] Net molecular charge, for gas default is 0. If None the charge is guessed by acpype.
            * **acpype_path** (*str*) - ("acpype") Path to the acpype executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **container_path** (*str*) - (None) Container path definition.
            * **container_image** (*str*) - ('mmbirb/acpype:latest') Container image definition.
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
    
    def __init__(self, input_path,  output_path_frcmod, output_path_inpcrd, output_path_lib, output_path_prmtop, 
                properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)

        # Input/Output files
        self.io_dict = { 
            "in": { "input_path": input_path }, 
            "out": { "output_path_frcmod": output_path_frcmod, "output_path_inpcrd": output_path_inpcrd, "output_path_lib": output_path_lib, "output_path_prmtop": output_path_prmtop } 
        }

        # Properties specific for BB
        self.basename = properties.get('basename', 'BBB')
        self.charge = properties.get('charge', '')
        self.acpype_path = get_binary_path(properties, 'acpype_path')
        self.properties = properties

        # Check the properties
        self.check_properties(properties)

    def check_data_params(self, out_log, err_log):
        """ Checks all the input/output paths and parameters """
        self.io_dict["in"]["input_path"] = check_input_path(self.io_dict["in"]["input_path"], out_log, self.__class__.__name__)
        self.io_dict["out"]["output_path_frcmod"] = check_output_path(self.io_dict["out"]["output_path_frcmod"], 'frcmod', out_log, self.__class__.__name__)
        self.io_dict["out"]["output_path_inpcrd"] = check_output_path(self.io_dict["out"]["output_path_inpcrd"], 'inpcrd', out_log, self.__class__.__name__)
        self.io_dict["out"]["output_path_lib"] = check_output_path(self.io_dict["out"]["output_path_lib"], 'lib', out_log, self.__class__.__name__)
        self.io_dict["out"]["output_path_prmtop"] = check_output_path(self.io_dict["out"]["output_path_prmtop"], 'prmtop', out_log, self.__class__.__name__)
        self.output_files = {
            'frcmod': self.io_dict["out"]["output_path_frcmod"],
            'inpcrd': self.io_dict["out"]["output_path_inpcrd"],
            'lib': self.io_dict["out"]["output_path_lib"],
            'prmtop': self.io_dict["out"]["output_path_prmtop"],
        }

    def create_cmd(self, container_io_dict, out_log, err_log):
        """Creates the command line instruction using the properties file settings"""
        instructions_list = []

        # generating output path
        if self.container_path:
            #instructions_list.append('cd ' + self.container_volume_path + ';')
            out_pth = self.container_volume_path + '/' + get_basename(self.basename, out_log) + '.' + self.unique_name
        else:
            out_pth = get_basename(self.basename, out_log) + '.' + self.unique_name

        # executable path
        instructions_list.append(self.acpype_path)

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

        return instructions_list

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`AcpypeParamsAC <acpype.acpype_params_ac.AcpypeParamsAC>` acpype.acpype_params_ac.AcpypeParamsAC object."""
        
        # check input/output paths and parameters
        self.check_data_params(self.out_log, self.err_log)

        # Setup Biobb
        if self.check_restart(): return 0
        self.stage_files()

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
            process_output(self.unique_name, 
                           self.stage_io_dict['unique_dir'], 
                           self.remove_tmp, 
                           self.basename, 
                           get_default_value(self.__class__.__name__), 
                           self.output_files, self.out_log)
        else:
            process_output(self.unique_name, 
                           self.basename + "." + self.unique_name + ".acpype", 
                           self.remove_tmp, 
                           self.basename, 
                           get_default_value(self.__class__.__name__), 
                           self.output_files, self.out_log)
        
        return self.return_code

def acpype_params_ac(input_path: str, output_path_frcmod: str, output_path_inpcrd: str, output_path_lib: str, output_path_prmtop: str, properties: dict = None, **kwargs) -> int:
    """Execute the :class:`AcpypeParamsAC <acpype.acpype_params_ac.AcpypeParamsAC>` class and
    execute the :meth:`launch() <acpype.acpype_params_ac.AcpypeParamsAC.launch>` method."""

    return AcpypeParamsAC(input_path=input_path, 
                    output_path_frcmod=output_path_frcmod, 
                    output_path_inpcrd=output_path_inpcrd,
                    output_path_lib=output_path_lib,
                    output_path_prmtop=output_path_prmtop,
                    properties=properties, **kwargs).launch()

def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description="Small molecule parameterization for AMBER MD package.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_path', required=True, help='Path to the input file. Accepted formats: pdb, mdl, mol2.')
    required_args.add_argument('--output_path_frcmod', required=True, help='Path to the FRCMOD output file. Accepted formats: frcmod.')
    required_args.add_argument('--output_path_inpcrd', required=True, help='Path to the INPCRD output file. Accepted formats: inpcrd.')
    required_args.add_argument('--output_path_lib', required=True, help='Path to the LIB output file. Accepted formats: lib.')
    required_args.add_argument('--output_path_prmtop', required=True, help='Path to the PRMTOP output file. Accepted formats: prmtop.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    # Specific call of each building block
    acpype_params_ac(input_path=args.input_path, 
                    output_path_frcmod=args.output_path_frcmod, 
                    output_path_inpcrd=args.output_path_inpcrd, 
                    output_path_lib=args.output_path_lib, 
                    output_path_prmtop=args.output_path_prmtop, 
                    properties=properties)

if __name__ == '__main__':
    main()
