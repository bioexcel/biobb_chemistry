#!/usr/bin/env python3

"""Module containing the Open Babel class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_common.command_wrapper import cmd_wrapper
from biobb_chemistry.babelm.common import *

class BabelMinimize():
    """Energetically minimize small molecules.
    Wrapper of the Open Babel module. Structure minimization.
    Open Babel is a chemical toolbox designed to speak the many languages of chemical data. It's an open, collaborative project 
    allowing anyone to search, convert, analyze, or store data from molecular modeling, chemistry, solid-state materials, 
    biochemistry, or related areas. `Visit the official page <http://openbabel.org/wiki/Main_Page>`_.

    Args:
        input_path (str): Path to the input file. File type: input. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/babel/babel.minimize.pdb>`_. Accepted formats: pdb, mol2.
        output_path (str): Path to the output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/babel/ref_babel.minimize.pdb>`_. Accepted formats: pdb, mol2.
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
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **container_path** (*str*) - (None) Container path definition.
            * **container_image** (*str*) - ('informaticsmatters/obabel:latest') Container image definition.
            * **container_volume_path** (*str*) - ('/tmp') Container volume path definition.
            * **container_working_dir** (*str*) - (None) Container working directory definition.
            * **container_user_id** (*str*) - (None) Container user_id definition.
            * **container_shell_path** (*str*) - ('/bin/bash') Path to default shell inside the container.
    """

    def __init__(self, input_path, output_path, properties=None, **kwargs):
        properties = properties or {}

        # Input/Output files
        self.io_dict = { 
            "in": { "input_path": check_input_path_minimize(input_path, self.__class__.__name__) }, 
            "out": { "output_path": check_output_path_minimize(output_path, self.__class__.__name__) } 
        }

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
        self.properties = properties

        # container Specific
        self.container_path = properties.get('container_path')
        self.container_image = properties.get('container_image', 'informaticsmatters/obabel:latest')
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

        iextension = PurePath(container_io_dict["in"]["input_path"]).suffix
        oextension = PurePath(container_io_dict["out"]["output_path"]).suffix

        instructions_list.append('-i' + iextension[1:] + ' ' + container_io_dict["in"]["input_path"])

        instructions_list.append('-o' + oextension[1:])

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
            output_file_list = [self.io_dict["out"]["output_path"]]
            if fu.check_complete_files(output_file_list):
                fu.log('Restart is enabled, this step: %s will the skipped' % self.step, out_log, self.global_log)
                return 0

        # copy inputs to container
        container_io_dict = fu.copy_to_container(self.container_path, self.container_volume_path, self.io_dict)

        # create and execute command line instruction
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
    parser = argparse.ArgumentParser(description="Energetically minimize small molecules.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_path', required=True, help='Path to the input file. Accepted formats: pdb, mol2.')
    required_args.add_argument('--output_path', required=True, help='Path to the output file. Accepted formats: pdb, mol2.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    # Specific call of each building block
    BabelMinimize(input_path=args.input_path, output_path=args.output_path, 
                  properties=properties).launch()

if __name__ == '__main__':
    main()
