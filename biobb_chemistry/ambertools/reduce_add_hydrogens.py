#!/usr/bin/env python3

"""Module containing the Open Babel class and the command line interface."""
import argparse
from biobb_common.configuration import settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_common.command_wrapper import cmd_wrapper
from biobb_chemistry.ambertools.common import *

class ReduceAddHydrogens():
    """Adds hydrogen atoms to small molecules.
    Wrapper of the Ambertools reduce module. Adds hydrogens to a given structure.
    Reduce is a program for `adding hydrogens to a Protein DataBank (PDB) molecular structure file <http://ambermd.org/doc12/AmberTools12.pdf>`_.

    Args:
        input_path (str): Path to the input file. File type: input. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/ambertools/reduce.no.H.pdb>`_. Accepted formats: pdb.
        output_path (str): Path to the output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/ambertools/ref_reduce.add.pdb>`_. Accepted formats: pdb.
        properties (dic):
            * **flip** (*bool*) - (False) add H and rotate and flip NQH groups
            * **noflip** (*bool*) - (False) add H and rotate groups with no NQH flips
            * **nuclear** (*bool*) - (False) use nuclear X-H distances rather than default electron cloud distances
            * **nooh** (*bool*) - (False) remove hydrogens on OH and SH groups
            * **oh** (*bool*) - (True) add hydrogens on OH and SH groups (default)
            * **his** (*bool*) - (False) create NH hydrogens on HIS rings (usually used with -HIS)
            * **noheth** (*bool*) - (False) do not attempt to add NH proton on Het groups
            * **rotnh3** (*bool*) - (True) allow lysine NH3 to rotate (default)
            * **norotnh3** (*bool*) - (False) do not allow lysine NH3 to rotate
            * **rotexist** (*bool*) - (False) allow existing rotatable groups (OH, SH, Met-CH3) to rotate
            * **rotexoh** (*bool*) - (False) allow existing OH & SH groups to rotate
            * **allalt** (*bool*) - (True) process adjustments for all conformations (default)
            * **onlya** (*bool*) - (False) only adjust 'A' conformations
            * **charges** (*bool*) - (False) output charge state for appropriate hydrogen records
            * **dorotmet** (*bool*) - (False) allow methionine methyl groups to rotate (not recommended)
            * **noadjust** (*bool*) - (False) do not process any rot or flip adjustments
            * **build** (*bool*) - (False) add H, including His sc NH, then rotate and flip groups (except for pre-existing methionine methyl hydrogens)
            * **reduce_path** (*str*) - ("reduce") Path to the reduce executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **container_path** (*str*) - (None) Container path definition.
            * **container_image** (*str*) - ('afandiadib/ambertools:serial') Container image definition.
            * **container_volume_path** (*str*) - ('/tmp') Container volume path definition.
            * **container_working_dir** (*str*) - (None) Container working directory definition.
            * **container_user_id** (*str*) - (None) Container user_id definition.
            * **container_shell_path** (*str*) - ('/bin/bash') Path to default shell inside the container.
    """

    def __init__(self, input_path, output_path, properties=None, **kwargs):
        properties = properties or {}

        # Input/Output files
        self.io_dict = { 
            "in": { "input_path": input_path }, 
            "out": { "output_path": output_path } 
        }

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
        self.properties = properties

        # container Specific
        self.container_path = properties.get('container_path')
        self.container_image = properties.get('container_image', 'afandiadib/ambertools:serial')
        self.container_volume_path = properties.get('container_volume_path', '/tmp')
        self.container_working_dir = properties.get('container_working_dir')
        self.container_user_id = properties.get('container_user_id')
        self.container_shell_path = properties.get('container_shell_path', '/bin/bash')

        # Properties common in all BB
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.global_log = properties.get('global_log', None)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')
        self.remove_tmp = properties.get('remove_tmp', True)
        self.restart = properties.get('restart', False)

    def create_cmd(self, container_io_dict, out_log, err_log):
        """Creates the command line instruction using the properties file settings"""
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

        instructions_list.append(container_io_dict["in"]["input_path"])
        instructions_list.append('>')
        instructions_list.append(container_io_dict["out"]["output_path"])

        return instructions_list

    @launchlogger
    def launch(self):
        """Launches the execution of the Open Babel module."""
       
        # Get local loggers from launchlogger decorator
        out_log = getattr(self, 'out_log', None)
        err_log = getattr(self, 'err_log', None)

        # Check the properties
        fu.check_properties(self, self.properties)

        if self.restart:
            output_file_list = [self.output_path]
            if fu.check_complete_files(output_file_list):
                fu.log('Restart is enabled, this step: %s will the skipped' % self.step, out_log, self.global_log)
                return 0

        # copy inputs to container
        container_io_dict = fu.copy_to_container(self.container_path, self.container_volume_path, self.io_dict)

        # create cmd and launch execution
        cmd = self.create_cmd(container_io_dict, out_log, err_log)
        cmd = fu.create_cmd_line(cmd, container_path=self.container_path, 
                                 host_volume=container_io_dict.get("unique_dir"), 
                                 container_volume=self.container_volume_path, 
                                 container_working_dir=self.container_working_dir, 
                                 container_user_uid=self.container_user_id, 
                                 container_image=self.container_image, 
                                 container_shell_path=self.container_shell_path, 
                                 out_log=out_log, global_log=self.global_log)
        returncode = cmd_wrapper.CmdWrapper(cmd, out_log, err_log, self.global_log).launch()

        # copy output(s) to output(s) path(s) in case of container execution
        fu.copy_to_host(self.container_path, container_io_dict, self.io_dict)

        # remove temporary folder(s)
        if self.container_path and self.remove_tmp: 
            fu.rm(container_io_dict['unique_dir'])
            fu.log('Removed: %s' % str(container_io_dict['unique_dir']), out_log)

        return returncode

def main():
    parser = argparse.ArgumentParser(description="Adds hydrogen atoms to small molecules.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_path', required=True, help='Path to the input file. Accepted formats: pdb.')
    required_args.add_argument('--output_path', required=True, help='Path to the output file. Accepted formats: pdb.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    # Specific call of each building block
    ReduceAddHydrogens(input_path=args.input_path, output_path=args.output_path, 
                       properties=properties).launch()

if __name__ == '__main__':
    main()
