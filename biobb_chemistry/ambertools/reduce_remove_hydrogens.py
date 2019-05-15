#!/usr/bin/env python3

"""Module containing the Open Babel class and the command line interface."""
import argparse
from biobb_common.configuration import settings
from biobb_common.tools import file_utils as fu
from biobb_common.command_wrapper import cmd_wrapper
from biobb_chemistry.ambertools.common import *

class ReduceRemoveHydrogens():
    """Wrapper of the Ambertools reduce module. Removes hydrogens to a given structure.
    Reduce is a program for adding hydrogens to a Protein DataBank (PDB) molecular structure file: http://ambermd.org/doc12/AmberTools12.pdf

    Args:
        input_path (str): Path to the input file. Accepted format: pdb.
        output_path (str): Path to the output file. Accepted format: pdb.
        properties (dic):
            * **reduce_path** (*str*) - ("reduce") Path to the reduce executable binary.
    """

    def __init__(self, input_path, output_path, properties=None, **kwargs):
        properties = properties or {}

        # Input/Output files
        self.input_path = check_input_path_reduce(input_path, self.__class__.__name__)
        self.output_path = check_output_path_reduce(output_path, self.__class__.__name__)

        # Properties specific for BB
        self.reduce_path = get_binary_path(properties, 'reduce_path')

        # Properties common in all BB
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.global_log = properties.get('global_log', None)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')

        # Check the properties
        fu.check_properties(self, properties)

    def create_cmd(self):
        """Creates the command line instruction using the properties file settings"""
        out_log, err_log = fu.get_logs(path=self.path, prefix=self.prefix, step=self.step, can_write_console=self.can_write_console_log)
        instructions_list = []

        # executable path
        instructions_list.append(self.reduce_path)

        instructions_list.append('-Trim')

        instructions_list.append(self.input_path)
        instructions_list.append('>')
        instructions_list.append(self.output_path)

        return instructions_list

    def launch(self):
        """Launches the execution of the Open Babel module."""
        out_log, err_log = fu.get_logs(path=self.path, prefix=self.prefix, step=self.step, can_write_console=self.can_write_console_log)

        # create command line instruction
        cmd = self.create_cmd()

        returncode = cmd_wrapper.CmdWrapper(cmd, out_log, err_log, self.global_log).launch()
        return returncode

def main():
    parser = argparse.ArgumentParser(description="Wrapper of the Ambertools reduce module. Removes hydrogens to a given structure.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')
    parser.add_argument('--system', required=False, help="Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help")
    parser.add_argument('--step', required=False, help="Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help")

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_path', required=True, help='Path to the input file. Accepted format: pdb.')
    required_args.add_argument('--output_path', required=True, help='Path to the output file. Accepted format: pdb.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config, system=args.system).get_prop_dic()
    if args.step:
        properties = properties[args.step]

    # Specific call of each building block
    ReduceRemoveHydrogens(input_path=args.input_path, output_path=args.output_path, properties=properties).launch()

if __name__ == '__main__':
    main()
