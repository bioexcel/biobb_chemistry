#!/usr/bin/env python3

"""Module containing the AcpypeConvertAMBERtoGMX class and the command line interface."""
from biobb_common.generic.biobb_object import BiobbObject
from biobb_chemistry.acpype.common import get_binary_path, get_basename, create_unique_name, get_default_value, process_output_gmx, get_acpype_options, get_acpype_options_cmd, AMB2GMX_OPTIONS
from typing import Optional
import os


class AcpypeConvertAMBERtoGMX(BiobbObject):
    """
    | biobb_chemistry AcpypeConvertAMBERtoGMX
    | This class is a wrapper of `Acpype <https://github.com/alanwilter/acpype>`_ tool for the conversion of AMBER topologies to GROMACS.
    | Acpype is a tool based in Python to use Antechamber to generate topologies for chemical compounds and to interface with others python applications like CCPN or ARIA. `Visit the official page <https://github.com/alanwilter/acpype>`_.

    Args:
        input_crd_path (str): Path to the input coordinates file (AMBER crd). File type: input. `Sample file <https://raw.githubusercontent.com/bioexcel/biobb_chemistry/master/biobb_chemistry/test/data/acpype/acpype.coords.inpcrd>`_. Accepted formats: inpcrd (edam:format_3878).
        input_top_path (str): Path to the input topology file (AMBER ParmTop). File type: input. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/acpype/acpype.top.prmtop>`_. Accepted formats: top (edam:format_3881), parmtop (edam:format_3881), prmtop (edam:format_3881).
        output_path_gro (str): Path to the GRO output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.amber2gmx.gro>`_. Accepted formats: gro (edam:format_2033).
        output_path_top (str): Path to the TOP output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.amber2gmx.top>`_. Accepted formats: top (edam:format_3880).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **basename** (*str*) - ("BBB") A basename for the project (folder and output files).
            * **gmx4** (*bool*) - (False) Write Ryckaert-Bellemans dihedrals for the old GROMACS 4.0.
            * **merge** (*bool*) - (False) Merge lower and uppercase atom types in the GROMACS topology if their parameters match.
            * **sorted** (*bool*) - (False) Sort atoms for the GROMACS ordering.
            * **split_molecules** (*bool*) - (False) Write one [ moleculetype ] per molecule found in the AMBER topology, ie: protein and ligand apart (not available in acpype 2023.10.27).
            * **direct** (*bool*) - (False) Do a direct conversion of any solvent (experimental).
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
        self.acpype_options = AMB2GMX_OPTIONS
        get_acpype_options(self, properties, self.acpype_options)
        self.properties = properties

        # Output files by extension, written by run() in the sandbox
        self.output_files = {
            'gro': "output_path_gro",
            'top': "output_path_top",
        }

    def create_cmd(self, container_io_dict, out_log, err_log):
        """Creates the command line instruction using the properties file settings"""
        instructions_list = []

        # generating output path
        self.basename = get_basename(self.basename, out_log)
        if self.container_path:
            self.container_working_dir = self.container_volume_path
            out_pth = self.basename + '.' + self.unique_name
            instructions_list.append('cd ' + self.container_volume_path + ' &&')
        else:
            out_pth = self.basename + '.' + self.unique_name

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

        # adding the acpype options
        instructions_list.extend(get_acpype_options_cmd(self, self.acpype_options, out_log, self.__class__.__name__))

        return instructions_list

    def run(self) -> None:
        """Execute the :class:`AcpypeConvertAMBERtoGMX <acpype.acpype_convert_amber_to_gmx.AcpypeConvertAMBERtoGMX>` acpype.acpype_convert_amber_to_gmx.AcpypeConvertAMBERtoGMX object."""

        # create unique name for temporary folder (created by acpype)
        self.unique_name = create_unique_name(6)

        # create command line instruction
        self.cmd = self.create_cmd(self.stage_io_dict, self.out_log, self.err_log)

        # Run Biobb block
        self.run_biobb()

        # Copy the files that acpype writes in its folder to the output paths, with the original name in them.
        output_files = {extension: self.sandbox_file(file_ref) for extension, file_ref in self.output_files.items()}
        if self.container_path or self.chdir_sandbox:
            process_output_gmx(self.unique_name,
                               os.path.join(self.stage_io_dict['unique_dir'], self.basename + "." + self.unique_name + ".amb2gmx"),
                               self.basename,
                               get_default_value(self.__class__.__name__),
                               output_files, self.out_log)
        else:
            self.tmp_files.append(self.basename + "." + self.unique_name + ".amb2gmx")
            process_output_gmx(self.unique_name,
                               self.basename + "." + self.unique_name + ".amb2gmx",
                               self.basename,
                               get_default_value(self.__class__.__name__),
                               output_files, self.out_log)


def acpype_convert_amber_to_gmx(input_crd_path: str, input_top_path: str, output_path_gro: str, output_path_top: str, properties: Optional[dict] = None, **kwargs) -> int:
    """Create the :class:`AcpypeConvertAMBERtoGMX <acpype.acpype_convert_amber_to_gmx.AcpypeConvertAMBERtoGMX>` class and
    execute the :meth:`launch() <acpype.acpype_convert_amber_to_gmx.AcpypeConvertAMBERtoGMX.launch>` method."""
    return AcpypeConvertAMBERtoGMX(**dict(locals())).launch()


acpype_convert_amber_to_gmx.__doc__ = AcpypeConvertAMBERtoGMX.__doc__
main = AcpypeConvertAMBERtoGMX.get_main(acpype_convert_amber_to_gmx, "Small molecule parameterization for GROMACS MD package.")

if __name__ == '__main__':
    main()
