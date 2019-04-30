#!/usr/bin/env python3

"""Module containing the Acpype class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.command_wrapper import cmd_wrapper
from biobb_chemistry.acpype.common import *

class AcpypeParamsGMX():
    """Wrapper for the Acpype module. Generation of topologies for GROMACS.
    Acpype is a tool based in Python to use Antechamber to generate topologies for chemical
    compounds and to interface with others python applications like CCPN or ARIA. 
    Visit the official page: https://github.com/alanwilter/acpype

    Args:
        input_path (str): Path to the input file. Accepted formats: pdb, mdl, mol2.
        output_path (str): Path to the output folder where the multiple input files will be saved.
        properties (dic):
            * **basename** (*str*) - ("BBB") A basename for the project (folder and output files).
            * **charge** (*int*) - (0) Net molecular charge, for gas default is 0.
            * **acpype_path** (*str*) - ("acpype") Path to the acpype executable binary.
    """

    def __init__(self, input_path, output_path, properties=None, **kwargs):
        properties = properties or {}

        # Input/Output files
        self.input_path = check_input_path(input_path)
        self.output_path = check_output_path(output_path)

        # Properties specific for BB
        self.basename = properties.get('basename', '')
        self.charge = properties.get('charge', '')
        self.acpype_path = get_binary_path(properties, 'acpype_path')

        # Properties common in all BB
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.global_log = properties.get('global_log', None)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')

    def create_cmd(self):
        """Creates the command line instruction using the properties file settings"""
        out_log, err_log = fu.get_logs(path=self.path, prefix=self.prefix, step=self.step, can_write_console=self.can_write_console_log)
        instructions_list = []

        # executable path
        instructions_list.append(self.acpype_path)

        # generating input 
        ipath = '-i ' + self.input_path
        instructions_list.append(ipath)

        # generating output 
        basename = '-b ' + get_basename(self.basename, out_log)
        instructions_list.append(basename)

        # CNS, GMX and AMBER
        # acpype -i ZEN.pdb -b ZEN -n 0 

        # adding charge
        charge = '-n ' + get_charge(self.charge, out_log)
        instructions_list.append(charge)

        """print(os.getcwd())

        os.chdir(self.output_path)

        print(os.getcwd())"""

        print(instructions_list)
        #raise SystemExit('exiting')

        return instructions_list

    def launch(self):
        """Launches the execution of the Open Babel module."""
        out_log, err_log = fu.get_logs(path=self.path, prefix=self.prefix, step=self.step, can_write_console=self.can_write_console_log)

        # create temporary folder
        ############################################
        # self.tmp_folder = fu.create_unique_dir()
        self.tmp_folder = '64b2e756-7c28-4463-941b-aba7d3fd9282'
        ############################################

        # create command line instruction
        ############################################
        # cmd = self.create_cmd() 
        cmd = ["ls"]
        ############################################

        # change execution directory to output_path
        ############################################
        # os.chdir(self.tmp_folder)
        ############################################

        # execute cmd
        returncode = cmd_wrapper.CmdWrapper(cmd, out_log, err_log, self.global_log).launch()
        # create here a function that changes directory, executes acpype, moves files and removes temporary folder
        # print(os.path.join(self.tmp_folder, self.basename + ".acpype"))
        # '64b2e756-7c28-4463-941b-aba7d3fd9282/BBB.acpype', 
        process_output(self.tmp_folder, self.basename + ".acpype", get_default_value(self.__class__.__name__), self.output_path, out_log)
        return returncode

def main():
    parser = argparse.ArgumentParser(description="Wrapper for the Acpype module. Generation of topologies for GROMACS.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')
    parser.add_argument('--system', required=False, help="Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help")
    parser.add_argument('--step', required=False, help="Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help")

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_path', required=True, help='Path to the input file. Accepted formats: pdb, mdl, mol2.')
    required_args.add_argument('--output_path', required=True, help='Path to the output folder where the multiple input files will be saved.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config, system=args.system).get_prop_dic()
    if args.step:
        properties = properties[args.step]

    # Specific call of each building block
    AcpypeParamsGMX(input_path=args.input_path, output_path=args.output_path, properties=properties).launch()

if __name__ == '__main__':
    main()
