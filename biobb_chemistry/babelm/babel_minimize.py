#!/usr/bin/env python3

"""Module containing the BabelMinimize class and the command line interface."""
import argparse
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import  settings
from biobb_common.tools.file_utils import launchlogger
from biobb_chemistry.babelm.common import *

class BabelMinimize(BiobbObject):
    """
    | biobb_chemistry BabelMinimize
    | This class is a wrapper of the Open Babel tool.
    | Energetically minimizes small molecules. Open Babel is a chemical toolbox designed to speak the many languages of chemical data. It's an open, collaborative project allowing anyone to search, convert, analyze, or store data from molecular modeling, chemistry, solid-state materials, biochemistry, or related areas. `Visit the official page <http://openbabel.org/wiki/Main_Page>`_.

    Args:
        input_path (str): Path to the input file. File type: input. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/babel/babel.minimize.pdb>`_. Accepted formats: pdb (edam:format_1476), mol2 (edam:format_3816).
        output_path (str): Path to the output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/babel/ref_babel.minimize.pdb>`_. Accepted formats: pdb (edam:format_1476), mol2 (edam:format_3816).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **criteria** (*float*) - (1e-6) Convergence criteria
            * **method** (*str*) - ("cg") Method. Values: cg (conjugate gradients algorithm), sd (steepest descent algorithm).
            * **force_field** (*str*) - (None) Force field. Values: GAFF (General Amber Force Field), Ghemical (Ghemical force field), MMFF94 (MMFF94 force field), MMFF94s (MMFF94s force field), UFF (Universal Force Field).
            * **hydrogens** (*bool*) - (False) Add hydrogen atoms.
            * **steps** (*int*) - (2500) [0~5000|1] Maximum number of steps.
            * **cutoff** (*bool*) - (False) Use cut-off.
            * **rvdw** (*float*) - (6.0) [0~50|1.0] VDW cut-off distance.
            * **rele** (*float*) - (10.0) [0~50|1.0] Electrostatic cut-off distance.
            * **frequency** (*int*) - (10) [0~50|1] Frequency to update the non-bonded pairs.
            * **obminimize_path** (*str*) - ("obminimize") Path to the obminimize executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **container_path** (*str*) - (None) Container path definition.
            * **container_image** (*str*) - ('informaticsmatters/obabel:latest') Container image definition.
            * **container_volume_path** (*str*) - ('/tmp') Container volume path definition.
            * **container_working_dir** (*str*) - (None) Container working directory definition.
            * **container_user_id** (*str*) - (None) Container user_id definition.
            * **container_shell_path** (*str*) - ('/bin/bash') Path to default shell inside the container.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_chemistry.babelm.babel_minimize import babel_minimize
            prop = { 
                'criteria': 1e-6, 
                'method': 'cg', 
                'force_field': 'GAFF' 
            }
            babel_minimize(input_path='/path/to/myStructure.mol2', 
                            output_path='/path/to/newStructure.mol2', 
                            properties=prop)

    Info:
        * wrapped_software:
            * name: Open Babel
            * version: 2.4.1
            * license: GNU
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, input_path, output_path, 
                properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)

        # Input/Output files
        self.io_dict = { 
            "in": { "input_path": input_path }, 
            "out": { "output_path": output_path } 
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

        # Check the properties
        self.check_properties(properties)

    def check_data_params(self, out_log, err_log):
        """ Checks all the input/output paths and parameters """
        self.io_dict["in"]["input_path"] = check_input_path_minimize(self.io_dict["in"]["input_path"], out_log, self.__class__.__name__)
        self.io_dict["out"]["output_path"] = check_output_path_minimize(self.io_dict["out"]["output_path"], out_log, self.__class__.__name__)

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
    def launch(self) -> int:
        """Execute the :class:`BabelMinimize <babelm.babel_minimize.BabelMinimize>` babelm.babel_minimize.BabelMinimize object."""
        
        # check input/output paths and parameters
        self.check_data_params(self.out_log, self.err_log)

        # Setup Biobb
        if self.check_restart(): return 0
        self.stage_files()

        # create command line instruction
        self.cmd = self.create_cmd(self.stage_io_dict, self.out_log, self.err_log) 

        # Run Biobb block
        self.run_biobb()

        # Copy files to host
        self.copy_to_host()

        # remove temporary folder(s)
        if self.container_path and self.remove_tmp: 
            self.tmp_files.append(self.stage_io_dict.get("unique_dir"))
            self.remove_tmp_files()

        return self.return_code

def babel_minimize(input_path: str, output_path: str, properties: dict = None, **kwargs) -> int:
    """Execute the :class:`BabelMinimize <babelm.babel_minimize.BabelMinimize>` class and
    execute the :meth:`launch() <babelm.babel_minimize.BabelMinimize.launch>` method."""

    return BabelMinimize(input_path=input_path, 
                    output_path=output_path,
                    properties=properties, **kwargs).launch()

def main():
    """Command line execution of this building block. Please check the command line documentation."""
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
    babel_minimize(input_path=args.input_path, 
                    output_path=args.output_path, 
                    properties=properties)

if __name__ == '__main__':
    main()
