#!/usr/bin/env python3

"""Module containing the ReduceRemoveHydrogens class and the command line interface."""
import argparse
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import settings
from biobb_common.tools.file_utils import launchlogger
from biobb_chemistry.ambertools.common import *


class ReduceRemoveHydrogens(BiobbObject):
    """
    | biobb_chemistry ReduceRemoveHydrogens
    | This class is a wrapper of the `Ambertools <http://ambermd.org/doc12/AmberTools12.pdf>`_ reduce module for removing hydrogens from a given structure.
    | Reduce is a program for `adding or removing hydrogens to a Protein DataBank (PDB) molecular structure file <http://ambermd.org/doc12/AmberTools12.pdf>`_.

    Args:
        input_path (str): Path to the input file. File type: input. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/ambertools/reduce.H.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_path (str): Path to the output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/ambertools/ref_reduce.remove.pdb>`_. Accepted formats: pdb (edam:format_1476).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **reduce_path** (*str*) - ("reduce") Path to the reduce executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **container_path** (*str*) - (None) Container path definition.
            * **container_image** (*str*) - ('afandiadib/ambertools:serial') Container image definition.
            * **container_volume_path** (*str*) - ('/tmp') Container volume path definition.
            * **container_working_dir** (*str*) - (None) Container working directory definition.
            * **container_user_id** (*str*) - (None) Container user_id definition.
            * **container_shell_path** (*str*) - ('/bin/bash') Path to default shell inside the container.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_chemistry.ambertools.reduce_remove_hydrogens import reduce_remove_hydrogens
            prop = { }
            reduce_remove_hydrogens(input_path='/path/to/myStructure.pdb', 
                                    output_path='/path/to/newStructure.pdb', 
                                    properties=prop)

    Info:
        * wrapped_software:
            * name: AmberTools Reduce
            * version: >=20.0
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
        self.reduce_path = get_binary_path(properties, 'reduce_path')
        self.properties = properties

        # Check the properties
        self.check_properties(properties)

    def check_data_params(self, out_log, err_log):
        """ Checks all the input/output paths and parameters """
        self.io_dict["in"]["input_path"] = check_input_path(self.io_dict["in"]["input_path"], out_log, self.__class__.__name__)
        self.io_dict["out"]["output_path"] = check_output_path(self.io_dict["out"]["output_path"], out_log, self.__class__.__name__)

    def create_cmd(self, container_io_dict, out_log, err_log):
        """Creates the command line instruction using the properties file settings"""
        instructions_list = []

        # executable path
        instructions_list.append(self.reduce_path)

        instructions_list.append('-Trim')

        instructions_list.append(container_io_dict["in"]["input_path"])
        instructions_list.append('>')
        instructions_list.append(container_io_dict["out"]["output_path"])

        return instructions_list

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`ReduceRemoveHydrogens <ambertools.reduce_remove_hydrogens.ReduceRemoveHydrogens>` ambertools.reduce_remove_hydrogens.ReduceRemoveHydrogens object."""
        
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

def reduce_remove_hydrogens(input_path: str, output_path: str, properties: dict = None, **kwargs) -> int:
    """Execute the :class:`ReduceRemoveHydrogens <ambertools.reduce_remove_hydrogens.ReduceRemoveHydrogens>` class and
    execute the :meth:`launch() <ambertools.reduce_remove_hydrogens.ReduceRemoveHydrogens.launch>` method."""

    return ReduceRemoveHydrogens(input_path=input_path, 
                    output_path=output_path,
                    properties=properties, **kwargs).launch()

def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description="Removes hydrogen atoms to small molecules.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_path', required=True, help='Path to the input file. Accepted formats: pdb.')
    required_args.add_argument('--output_path', required=True, help='Path to the output file. Accepted formats: pdb.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    # Specific call of each building block
    reduce_remove_hydrogens(input_path=args.input_path, 
                            output_path=args.output_path, 
                            properties=properties)

if __name__ == '__main__':
    main()
