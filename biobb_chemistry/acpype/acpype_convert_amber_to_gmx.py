#!/usr/bin/env python3

"""Module containing the AcpypeConvertAMBERtoGMX class and the command line interface."""
import argparse
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import settings
from biobb_common.tools.file_utils import launchlogger
from biobb_chemistry.acpype.common import get_binary_path, check_output_path, get_basename, create_unique_name, get_default_value, process_output_gmx
from typing import Optional


class AcpypeConvertAMBERtoGMX(BiobbObject):
    """
    | biobb_chemistry AcpypeConvertAMBERtoGMX
    | This class is a wrapper of `Acpype <https://github.com/alanwilter/acpype>`_ tool for the conversion of AMBER topologies to GROMACS.
    | Acpype is a tool based in Python to use Antechamber to generate topologies for chemical compounds and to interface with others python applications like CCPN or ARIA. `Visit the official page <https://github.com/alanwilter/acpype>`_.

    Args:
        input_crd_path (str): Path to the input coordinates file (AMBER crd). File type: input. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.ac.container.inpcrd>`_. Accepted formats: inpcrd (edam:format_3878).
        input_top_path (str): Path to the input topology file (AMBER ParmTop). File type: input. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.ac.container.prmtop>`_. Accepted formats: top (edam:format_3881), parmtop (edam:format_3881), prmtop (edam:format_3881).
        output_path_gro (str): Path to the GRO output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.gmx.gro>`_. Accepted formats: gro (edam:format_2033).
        output_path_top (str): Path to the TOP output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.gmx.top>`_. Accepted formats: top (edam:format_3880).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **basename** (*str*) - ("BBB") A basename for the project (folder and output files).
            * **binary_path** (*str*) - ("acpype") Path to the acpype executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **container_path** (*str*) - (None) Container path definition.
            * **container_image** (*str*) - ('acpype/acpype:2022.7.21') Container image definition.
            * **container_volume_path** (*str*) - ('/tmp') Container volume path definition.
            * **container_working_dir** (*str*) - (None) Container working directory definition.
            * **container_user_id** (*str*) - (None) Container user_id definition.
            * **container_shell_path** (*str*) - ('/bin/bash') Path to default shell inside the container.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_chemistry.acpype.acpype_convert_amber_to_gmx import acpype_convert_amber_to_gmx
            prop = {
                'basename': 'BBB',
            }
            acpype_convert_amber_to_gmx(input_crd_path='/path/to/myStructure.inpcrd',
                            input_top_path='/path/to/myStructure.prmtop',
                            output_path_gro='/path/to/newGRO.gro',
                            output_path_top='/path/to/newTOP.top',
                            properties=prop)

    Info:
        * wrapped_software:
            * name: Acpype
            * version: 2019.10.05.12.26
            * license: GNU
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, input_crd_path, input_top_path, output_path_gro, output_path_top,
                 properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = {
            "in": {"input_crd_path": input_crd_path, "input_top_path": input_top_path},
            "out": {"output_path_gro": output_path_gro, "output_path_top": output_path_top}
        }

        # Properties specific for BB
        self.basename = properties.get('basename', 'BBB')
        self.binary_path = get_binary_path(properties, 'binary_path')
        self.properties = properties

        # Check the properties
        self.check_properties(properties)
        self.check_arguments()

    def check_data_params(self, out_log, err_log):
        """ Checks all the input/output paths and parameters """
        # NOTE: missing check input paths
        self.io_dict["out"]["output_path_gro"] = check_output_path(self.io_dict["out"]["output_path_gro"], 'gro', out_log, self.__class__.__name__)
        self.io_dict["out"]["output_path_top"] = check_output_path(self.io_dict["out"]["output_path_top"], 'top', out_log, self.__class__.__name__)
        self.output_files = {
            'gro': self.io_dict["out"]["output_path_gro"],
            'top': self.io_dict["out"]["output_path_top"],
        }

    def create_cmd(self, container_io_dict, out_log, err_log):
        """Creates the command line instruction using the properties file settings"""
        instructions_list = []

        # generating output path
        if self.container_path:
            out_pth = self.container_volume_path + '/' + get_basename(self.basename, out_log) + '.' + self.unique_name
        else:
            out_pth = get_basename(self.basename, out_log) + '.' + self.unique_name

        # executable path
        instructions_list.append(self.binary_path)

        # generating inputs
        crdpath = '-x ' + container_io_dict["in"]["input_crd_path"]
        instructions_list.append(crdpath)
        prmtopath = '-p ' + container_io_dict["in"]["input_top_path"]
        instructions_list.append(prmtopath)

        # generating output
        basename = '-b ' + out_pth
        instructions_list.append(basename)

        return instructions_list

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`AcpypeConvertAMBERtoGMX <acpype.acpype_convert_amber_to_gmx.AcpypeConvertAMBERtoGMX>` acpype.acpype_convert_amber_to_gmx.AcpypeConvertAMBERtoGMX object."""

        # check input/output paths and parameters
        self.check_data_params(self.out_log, self.err_log)

        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        # create unique name for temporary folder (created by acpype)
        self.unique_name = create_unique_name(6)

        # create command line instruction
        self.cmd = self.create_cmd(self.stage_io_dict, self.out_log, self.err_log)

        # Run Biobb block
        self.run_biobb()

        # Copy files to host
        self.copy_to_host()

        # move files to output_path and removes temporary folder
        if self.container_path:
            process_output_gmx(self.unique_name,
                               self.stage_io_dict['unique_dir'],
                               self.remove_tmp,
                               self.basename,
                               get_default_value(self.__class__.__name__),
                               self.output_files, self.out_log)
        else:
            process_output_gmx(self.unique_name,
                               self.basename + "." + self.unique_name + ".amb2gmx",
                               self.remove_tmp,
                               self.basename,
                               get_default_value(self.__class__.__name__),
                               self.output_files, self.out_log)

        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code


def acpype_convert_amber_to_gmx(input_crd_path: str, input_top_path: str, output_path_gro: str, output_path_top: str, properties: Optional[dict] = None, **kwargs) -> int:
    """Execute the :class:`AcpypeConvertAMBERtoGMX <acpype.acpype_convert_amber_to_gmx.AcpypeConvertAMBERtoGMX>` class and
    execute the :meth:`launch() <acpype.acpype_convert_amber_to_gmx.AcpypeConvertAMBERtoGMX.launch>` method."""

    return AcpypeConvertAMBERtoGMX(input_crd_path=input_crd_path,
                                   input_top_path=input_top_path,
                                   output_path_gro=output_path_gro,
                                   output_path_top=output_path_top,
                                   properties=properties, **kwargs).launch()


def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description="Small molecule parameterization for GROMACS MD package.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_crd_path', required=True, help='Path to the input coordinates file (AMBER crd). Accepted formats: inpcrd.')
    required_args.add_argument('--input_top_path', required=True, help='Path to the input topology file (AMBER ParmTop). Accepted formats: top, parmtop, prmtop.')
    required_args.add_argument('--output_path_gro', required=True, help='Path to the GRO output file. Accepted formats: gro.')
    required_args.add_argument('--output_path_top', required=True, help='Path to the TOP output file. Accepted formats: top.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    # Specific call of each building block
    acpype_convert_amber_to_gmx(input_crd_path=args.input_crd_path,
                                input_top_path=args.input_top_path,
                                output_path_gro=args.output_path_gro,
                                output_path_top=args.output_path_top,
                                properties=properties)


if __name__ == '__main__':
    main()
