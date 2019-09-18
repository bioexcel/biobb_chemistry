#!/usr/bin/env python3

"""Module containing the Acpype class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_common.command_wrapper import cmd_wrapper
from biobb_chemistry.acpype.common import *

class AcpypeParamsAC():
    """Small molecule parameterization for AMBER MD package.
    Wrapper for the Acpype module. Generation of topologies for Antechamber.
    Acpype is a tool based in Python to use Antechamber to generate topologies for chemical
    compounds and to interface with others python applications like CCPN or ARIA. 
    Visit the official page: https://github.com/alanwilter/acpype

    Args:
        input_path (str): Path to the input file. Accepted formats: pdb, mdl, mol2.
        output_path_frcmod (str): Path to the FRCMOD output file. Accepted formats: frcmod.
        output_path_inpcrd (str): Path to the INPCRD output file. Accepted formats: inpcrd.
        output_path_lib (str): Path to the LIB output file. Accepted formats: lib.
        output_path_prmtop (str): Path to the PRMTOP output file. Accepted formats: prmtop.
        properties (dic):
            * **basename** (*str*) - ("BBB") A basename for the project (folder and output files).
            * **charge** (*int*) - (0) Net molecular charge, for gas default is 0.
            * **acpype_path** (*str*) - ("acpype") Path to the acpype executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
    """
    
    def __init__(self, input_path, output_path_frcmod, output_path_inpcrd, output_path_lib, output_path_prmtop, properties=None, **kwargs):
        properties = properties or {}

        # Input/Output files
        self.input_path = input_path
        self.output_path_frcmod = output_path_frcmod
        self.output_path_inpcrd = output_path_inpcrd
        self.output_path_lib = output_path_lib
        self.output_path_prmtop = output_path_prmtop

        # Properties specific for BB
        self.basename = properties.get('basename', '')
        self.charge = properties.get('charge', '')
        self.acpype_path = get_binary_path(properties, 'acpype_path')
        self.properties = properties

        # Properties common in all BB
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.global_log = properties.get('global_log', None)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')
        self.remove_tmp = properties.get('remove_tmp', True)
        self.restart = properties.get('restart', False)

    def check_data_params(self, out_log, err_log):
        """ Checks all the input/output paths and parameters """
        self.input_path = check_input_path(self.input_path, out_log, self.__class__.__name__)
        self.output_path_frcmod = check_output_path(self.output_path_frcmod, 'frcmod', out_log, self.__class__.__name__)
        self.output_path_inpcrd = check_output_path(self.output_path_inpcrd, 'inpcrd', out_log, self.__class__.__name__)
        self.output_path_lib = check_output_path(self.output_path_lib, 'lib', out_log, self.__class__.__name__)
        self.output_path_prmtop = check_output_path(self.output_path_prmtop, 'prmtop', out_log, self.__class__.__name__)
        self.output_files = {
            'frcmod': self.output_path_frcmod,
            'inpcrd': self.output_path_inpcrd,
            'lib': self.output_path_lib,
            'prmtop': self.output_path_prmtop,
        }

    def create_cmd(self, out_log, err_log):
        """Creates the command line instruction using the properties file settings"""
        instructions_list = []

        # executable path
        instructions_list.append(self.acpype_path)

        # generating input 
        ipath = '-i ' + self.input_path
        instructions_list.append(ipath)

        # generating output 
        basename = '-b ' + get_basename(self.basename, out_log) + '.' + self.unique_name
        instructions_list.append(basename)

        # adding charge
        charge = '-n ' + get_charge(self.charge, out_log)
        instructions_list.append(charge)

        return instructions_list

    @launchlogger
    def launch(self):
        """Launches the execution of the Open Babel module."""
        
        # Get local loggers from launchlogger decorator
        out_log = getattr(self, 'out_log', None)
        err_log = getattr(self, 'err_log', None)

        # check input/output paths and parameters
        self.check_data_params(out_log, err_log)

        # Check the properties
        fu.check_properties(self, self.properties)

        if self.restart:
            output_file_list = [self.output_path_frcmod, self.output_path_inpcrd, self.output_path_lib, self.output_path_prmtop]
            if fu.check_complete_files(output_file_list):
                fu.log('Restart is enabled, this step: %s will the skipped' % self.step, out_log, self.global_log)
                return 0

        # create unique name for temporary folder (created by acpype)
        self.unique_name = create_unique_name()

        # create command line instruction
        cmd = self.create_cmd(out_log, err_log) 

        # execute cmd
        fu.log('Running %s, this execution can take a while' % self.acpype_path, out_log)
        returncode = cmd_wrapper.CmdWrapper(cmd, out_log, err_log, self.global_log).launch()
        # move files to output_path and removes temporary folder
        process_output(self.unique_name, self.basename + "." + self.unique_name + ".acpype", self.remove_tmp, self.basename, get_default_value(self.__class__.__name__), self.output_files, out_log)
        return returncode

def main():
    parser = argparse.ArgumentParser(description="Small molecule parameterization for AMBER MD package.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')
    parser.add_argument('--system', required=False, help="Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help")
    parser.add_argument('--step', required=False, help="Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help")

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_path', required=True, help='Path to the input file. Accepted formats: pdb, mdl, mol2.')
    required_args.add_argument('--output_path_frcmod', required=True, help='Path to the FRCMOD output file. Accepted formats: frcmod.')
    required_args.add_argument('--output_path_inpcrd', required=True, help='Path to the INPCRD output file. Accepted formats: inpcrd.')
    required_args.add_argument('--output_path_lib', required=True, help='Path to the LIB output file. Accepted formats: lib.')
    required_args.add_argument('--output_path_prmtop', required=True, help='Path to the PRMTOP output file. Accepted formats: prmtop.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config, system=args.system).get_prop_dic()
    if args.step:
        properties = properties[args.step]

    # Specific call of each building block
    AcpypeParamsAC(input_path=args.input_path, output_path_frcmod=args.output_path_frcmod, output_path_inpcrd=args.output_path_inpcrd, output_path_lib=args.output_path_lib, output_path_prmtop=args.output_path_prmtop, properties=properties).launch()

if __name__ == '__main__':
    main()
