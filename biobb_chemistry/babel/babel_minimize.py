#!/usr/bin/env python3

"""Module containing the Open Babel class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.command_wrapper import cmd_wrapper
from biobb_chemistry.babel.common import *

class Convert():
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
    """

    def __init__(self, input_path, output_path, properties=None, **kwargs):
        properties = properties or {}

        # Input/Output files
        self.input_path = check_input_path(input_path)
        self.output_path = check_output_path(output_path)

        # Properties specific for BB
        self.input_format = get_parameters(properties, 'input_format')
        self.output_format = get_parameters(properties, 'output_format')
        self.coordinates = properties.get('coordinates', '')
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

        # generating input 
        infr = get_input_format(self)
        iformat = '-i' + infr
        instructions_list.append(iformat)
        ipath = self.input_path
        instructions_list.append(ipath)

        # generating output 
        oufr = get_output_format(self)
        oformat = '-o' + oufr
        instructions_list.append(oformat)
        opath = '-O' + self.output_path
        instructions_list.append(opath)

        # adding coordinates
        crd = get_coordinates(self)
        coordinates = ''
        if crd:
            coordinates = '--gen' + crd + 'D'

        instructions_list.append(coordinates)

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
    Convert(input_path=args.input_path, output_path=args.output_path, properties=properties).launch()

if __name__ == '__main__':
    main()
