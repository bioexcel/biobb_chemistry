#!/usr/bin/env python3

"""Module containing the ReduceAddHydrogens class and the command line interface."""
import argparse
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import settings
from biobb_common.tools.file_utils import launchlogger
from biobb_chemistry.ambertools.common import *


class ReduceAddHydrogens(BiobbObject):
    """
    | biobb_chemistry ReduceAddHydrogens
    | This class is a wrapper of the `Ambertools <http://ambermd.org/doc12/AmberTools12.pdf>`_ reduce module for adding hydrogens to a given structure.
    | Reduce is a program for `adding or removing hydrogens to a Protein DataBank (PDB) molecular structure file <http://ambermd.org/doc12/AmberTools12.pdf>`_.

    Args:
        input_path (str): Path to the input file. File type: input. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/ambertools/reduce.no.H.pdb>`_. Accepted formats: pdb (edam:format_1476).
        output_path (str): Path to the output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/ambertools/ref_reduce.add.pdb>`_. Accepted formats: pdb (edam:format_1476).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
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
            * **metal_bump** (*float*) - (None) [0~5|0.005] H 'bumps' metals at radius plus this
            * **non_metal_bump** (*float*) - (None) [0~5|0.005] 'bumps' nonmetal at radius plus this
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

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_chemistry.ambertools.reduce_add_hydrogens import reduce_add_hydrogens
            prop = { 
                'flip': False, 
                'charges': True, 
                'build': False 
            }
            reduce_add_hydrogens(input_path='/path/to/myStructure.pdb', 
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
        self.metal_bump = properties.get('metal_bump', None)
        self.non_metal_bump = properties.get('non_metal_bump', None)
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

        if self.metal_bump:
            instructions_list.append('-METALBump ' + str(self.metal_bump))

        if self.non_metal_bump:
            instructions_list.append('-NONMETALBump ' + str(self.non_metal_bump))

        instructions_list.append(container_io_dict["in"]["input_path"])
        instructions_list.append('>')
        instructions_list.append(container_io_dict["out"]["output_path"])

        return instructions_list

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`ReduceAddHydrogens <ambertools.reduce_add_hydrogens.ReduceAddHydrogens>` ambertools.reduce_add_hydrogens.ReduceAddHydrogens object."""
       
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

def reduce_add_hydrogens(input_path: str, output_path: str, properties: dict = None, **kwargs) -> int:
    """Execute the :class:`ReduceAddHydrogens <ambertools.reduce_add_hydrogens.ReduceAddHydrogens>` class and
    execute the :meth:`launch() <ambertools.reduce_add_hydrogens.ReduceAddHydrogens.launch>` method."""

    return ReduceAddHydrogens(input_path=input_path, 
                    output_path=output_path,
                    properties=properties, **kwargs).launch()

def main():
    """Command line execution of this building block. Please check the command line documentation."""
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
    reduce_add_hydrogens(input_path=args.input_path, 
                        output_path=args.output_path, 
                        properties=properties)

if __name__ == '__main__':
    main()
