#!/usr/bin/env python3

"""Module containing the Open Babel class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.command_wrapper import cmd_wrapper
from biobb_chemistry.babel.common import *

class BabelMinimize():
    """Wrapper of the Open Babel module.
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
            * **obabel_path** (*str*) - ("obabel") Path to the obabel executable binary.
    """

    def __init__(self, input_path, output_path, properties=None, **kwargs):
        properties = properties or {}

        # Input/Output files
        self.input_path = check_input_path(input_path)
        self.output_path = check_output_path(output_path)

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
        self.obabel_path = get_binary_path(properties, 'obabel_path')

        # Properties common in all BB
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.global_log = properties.get('global_log', None)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')

    def create_cmd(self):
        """Creates the command line instruction using the properties file settings"""
        instructions_list = []

        # obminimize -ff UFF -newton -c 0.000008 -ipdb output.pdb -opdb > smth.pd

        # executable path
        instructions_list.append(self.obabel_path)

        if self.criteria: instructions_list.append('-c ' + self.criteria)

        #if self.method: instructions_list.append('-c ' + self.method)

        if self.force_field: instructions_list.append('-ff ' + self.force_field)

        if self.hydrogens: instructions_list.append('-h')

        if self.steps: instructions_list.append('-n ' + str(self.steps))

        if self.cutoff: instructions_list.append('-cut')

        if self.rvdw: instructions_list.append('-rvdw ' + str(self.rvdw))

        if self.rele: instructions_list.append('-rele ' + str(self.rele))

        if self.frequency: instructions_list.append('-pf ' + str(self.frequency))

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
    parser = argparse.ArgumentParser(description="Wrapper for the Open Babel module.")
    parser.add_argument('--config', required=True, help='Configuration file')
    parser.add_argument('--system', required=False)
    parser.add_argument('--step', required=False)

    # Specific args of each building block
    parser.add_argument('--input_path', required=True, help='Path to the input file.')
    parser.add_argument('--output_path', required=True, help='Path to the output file.')

    args = parser.parse_args()
    check_conf(args.config)
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config, system=args.system).get_prop_dic()
    if args.step:
        properties = properties[args.step]

    # Specific call of each building block
    BabelMinimize(input_path=args.input_path, output_path=args.output_path, properties=properties).launch()

if __name__ == '__main__':
    main()
