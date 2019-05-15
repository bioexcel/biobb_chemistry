#!/usr/bin/env python3

"""Module containing the Open Babel class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.command_wrapper import cmd_wrapper
from biobb_chemistry.babelm.common import *

class BabelMinimize():
    """Wrapper of the Open Babel module. Structure minimization.
    Open Babel is a chemical toolbox designed to speak the many languages of chemical data. It's an open, collaborative project 
    allowing anyone to search, convert, analyze, or store data from molecular modeling, chemistry, solid-state materials, 
    biochemistry, or related areas. Visit the official page: http://openbabel.org/wiki/Main_Page

    Args:
        input_path (str): Path to the input file. Accepted format: pdb
        output_path (str): Path to the output file. Accepted format: pdb
        properties (dic):
            * **criteria** (*float*) - (1e-6) Convergence criteria
            * **method** (*str*) - ("cg") Method. Values: cg (conjugate gradients algorithm), sd (steepest descent algorithm).
            * **force_field** (*str*) - (None) Force field. Values: GAFF (General Amber Force Field), Ghemical (Ghemical force field), MMFF94 (MMFF94 force field), MMFF94s (MMFF94s force field), UFF (Universal Force Field).
            * **hydrogens** (*bool*) - (False) Add hydrogen atoms.
            * **steps** (*int*) - (2500) Maximum number of steps.
            * **cutoff** (*bool*) - (False) Use cut-off.
            * **rvdw** (*float*) - (6.0) VDW cut-off distance.
            * **rele** (*float*) - (10.0) Electrostatic cut-off distance.
            * **frequency** (*int*) - (10) Frequency to update the non-bonded pairs.
            * **obminimize_path** (*str*) - ("obminimize") Path to the obminimize executable binary.
    """

    def __init__(self, input_path, output_path, properties=None, **kwargs):
        properties = properties or {}

        # Input/Output files
        self.input_path = check_input_path_minimize(input_path, self.__class__.__name__)
        self.output_path = check_output_path_minimize(output_path, self.__class__.__name__)

        # Properties specific for BB
        self.criteria = properties.get('criteria', '')
        self.method = properties.get('method', '')
        self.force_field = properties.get('force_field', '')
        self.hydrogens = properties.get('hydrogens', '')
        self.steps = properties.get('steps', '')
        self.cutoff = properties.get('cutoff', '')
        self.rvdw = properties.get('rvdw', '')
        self.rele = properties.get('rele', '')
        self.frequency = properties.get('frequency', '')
        self.obminimize_path = get_binary_path(properties, 'obminimize_path')

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
        instructions_list.append(self.obminimize_path)

        # check all properties
        if check_minimize_property("criteria", self.criteria, out_log): instructions_list.append('-c ' + str(self.criteria))

        if check_minimize_property("method", self.method, out_log): instructions_list.append('-' + self.method)

        if check_minimize_property("force_field", self.force_field, out_log): instructions_list.append('-ff ' + self.force_field)

        if check_minimize_property("hydrogens", self.hydrogens, out_log): instructions_list.append('-h')

        if check_minimize_property("steps", self.steps, out_log): instructions_list.append('-n ' + str(self.steps))

        if check_minimize_property("cutoff", self.cutoff, out_log): instructions_list.append('-cut')

        if check_minimize_property("rvdw", self.rvdw, out_log): instructions_list.append('-rvdw ' + str(self.rvdw))

        if check_minimize_property("rele", self.rele, out_log): instructions_list.append('-rele ' + str(self.rele))

        if check_minimize_property("frequency", self.frequency, out_log): instructions_list.append('-pf ' + str(self.frequency))

        instructions_list.append('-ipdb ' + self.input_path)

        instructions_list.append('-opdb')

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
    parser = argparse.ArgumentParser(description="Wrapper for the Open Babel module. Structure minimization.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')
    parser.add_argument('--system', required=False, help="Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help")
    parser.add_argument('--step', required=False, help="Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help")

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_path', required=True, help='Path to the input file.')
    required_args.add_argument('--output_path', required=True, help='Path to the output file.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config, system=args.system).get_prop_dic()
    if args.step:
        properties = properties[args.step]

    # Specific call of each building block
    BabelMinimize(input_path=args.input_path, output_path=args.output_path, properties=properties).launch()

if __name__ == '__main__':
    main()
