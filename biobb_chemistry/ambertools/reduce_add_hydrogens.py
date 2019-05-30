#!/usr/bin/env python3

"""Module containing the Open Babel class and the command line interface."""
import argparse
from biobb_common.configuration import settings
from biobb_common.tools import file_utils as fu
from biobb_common.command_wrapper import cmd_wrapper
from biobb_chemistry.ambertools.common import *

class ReduceAddHydrogens():
    """Wrapper of the Ambertools reduce module. Adds hydrogens to a given structure.
    Reduce is a program for adding hydrogens to a Protein DataBank (PDB) molecular structure file: http://ambermd.org/doc12/AmberTools12.pdf

    Args:
        input_path (str): Path to the input file. Accepted format: pdb.
        output_path (str): Path to the output file. Accepted format: pdb.
        properties (dic):
            * **flip** (*Boolean*) - (False) add H and rotate and flip NQH groups
            * **noflip** (*Boolean*) - (False) add H and rotate groups with no NQH flips
            * **nuclear** (*Boolean*) - (False) use nuclear X-H distances rather than default electron cloud distances
            * **nooh** (*Boolean*) - (False) remove hydrogens on OH and SH groups
            * **oh** (*Boolean*) - (True) add hydrogens on OH and SH groups (default)
            * **his** (*Boolean*) - (False) create NH hydrogens on HIS rings (usually used with -HIS)
            * **noheth** (*Boolean*) - (False) do not attempt to add NH proton on Het groups
            * **rotnh3** (*Boolean*) - (True) allow lysine NH3 to rotate (default)
            * **norotnh3** (*Boolean*) - (False) do not allow lysine NH3 to rotate
            * **rotexist** (*Boolean*) - (False) allow existing rotatable groups (OH, SH, Met-CH3) to rotate
            * **rotexoh** (*Boolean*) - (False) allow existing OH & SH groups to rotate
            * **allalt** (*Boolean*) - (True) process adjustments for all conformations (default)
            * **onlya** (*Boolean*) - (False) only adjust 'A' conformations
            * **charges** (*Boolean*) - (False) output charge state for appropriate hydrogen records
            * **dorotmet** (*Boolean*) - (False) allow methionine methyl groups to rotate (not recommended)
            * **noadjust** (*Boolean*) - (False) do not process any rot or flip adjustments
            * **build** (*Boolean*) - (False) add H, including His sc NH, then rotate and flip groups (except for pre-existing methionine methyl hydrogens)
            * **reduce_path** (*str*) - ("reduce") Path to the reduce executable binary.
    """

    def __init__(self, input_path, output_path, properties=None, **kwargs):
        properties = properties or {}

        # Input/Output files
        self.input_path = check_input_path_reduce(input_path, self.__class__.__name__)
        self.output_path = check_output_path_reduce(output_path, self.__class__.__name__)

        # Properties specific for BB
        self.flip = properties.get('flip', False)
        self.noflip = properties.get('noflip', False)
        self.nuclear = properties.get('nuclear', False)
        self.nooh = properties.get('nooh', False)
        self.oh = properties.get('oh', True)
        self.his = properties.get('his', False)
        self.noheth = properties.get('noheth', False)
        self.rotnh3 = properties.get('rotnh3', True)
        self.norotnh3 = properties.get('norotnh3', False)
        self.rotexist = properties.get('rotexist', False)
        self.rotexoh = properties.get('rotexoh', False)
        self.allalt = properties.get('allalt', True)
        self.onlya = properties.get('onlya', False)
        self.charges = properties.get('charges', False)
        self.dorotmet = properties.get('dorotmet', False)
        self.noadjust = properties.get('noadjust', False)
        self.build = properties.get('build', False)
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

        if self.flip: instructions_list.append('-FLIP')
        if self.noflip: instructions_list.append('-NOFLIP')
        if self.nuclear: instructions_list.append('-NUClear')
        if self.nooh: instructions_list.append('-NOOH')
        if self.oh: instructions_list.append('-OH')
        if self.his: instructions_list.append('-HIS')
        if self.noheth: instructions_list.append('-NOHETh')
        if self.rotnh3: instructions_list.append('-ROTNH3')
        if self.norotnh3: instructions_list.append('-NOROTNH3')
        if self.rotexist: instructions_list.append('-ROTEXist')
        if self.rotexoh: instructions_list.append('-ROTEXOH')
        if self.allalt: instructions_list.append('-ALLALT')
        if self.onlya: instructions_list.append('-ONLYA')
        if self.charges: instructions_list.append('-CHARGEs')
        if self.dorotmet: instructions_list.append('-DOROTMET')
        if self.noadjust: instructions_list.append('-NOADJust')
        if self.build: instructions_list.append('-BUILD')

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
    parser = argparse.ArgumentParser(description="Wrapper of the Ambertools reduce module. Adds hydrogens to a given structure.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
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
    ReduceAddHydrogens(input_path=args.input_path, output_path=args.output_path, properties=properties).launch()

if __name__ == '__main__':
    main()
