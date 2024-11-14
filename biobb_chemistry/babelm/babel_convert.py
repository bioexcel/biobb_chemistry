#!/usr/bin/env python3

"""Module containing the BabelConvert class and the command line interface."""

import argparse
from typing import Optional

from biobb_common.configuration import settings
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools.file_utils import launchlogger

from biobb_chemistry.babelm.common import (
    _from_string_to_list,
    check_input_path,
    check_output_path,
    get_coordinates,
    get_input_format,
    get_output_format,
    get_ph,
)


class BabelConvert(BiobbObject):
    """
    | biobb_chemistry BabelConvert
    | This class is a wrapper of the Open Babel tool.
    | Small molecule format conversion for structures or trajectories. Open Babel is a chemical toolbox designed to speak the many languages of chemical data. It's an open, collaborative project allowing anyone to search, convert, analyze, or store data from molecular modeling, chemistry, solid-state materials, biochemistry, or related areas. `Visit the official page <http://openbabel.org/wiki/Main_Page>`_.

    Args:
        input_path (str): Path to the input file. File type: input. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/babel/babel.smi>`_. Accepted formats: dat (edam:format_1637), ent (edam:format_1476), fa (edam:format_1929), fasta (edam:format_1929), gro (edam:format_2033), inp (edam:format_3878), log (edam:format_2030), mcif (edam:format_1477), mdl (edam:format_3815), mmcif (edam:format_1477), mol (edam:format_3815), mol2 (edam:format_3816), pdb (edam:format_1476), pdbqt (edam:format_1476), png (edam:format_3603), sdf (edam:format_3814), smi (edam:format_1196), smiles (edam:format_1196), txt (edam:format_2033), xml (edam:format_2332), xtc (edam:format_3875).
        output_path (str): Path to the output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/babel/ref_babel.convert.mol2>`_. Accepted formats: ent (edam:format_1476), fa (edam:format_1929), fasta (edam:format_1929), gro (edam:format_2033), inp (edam:format_3878), mcif (edam:format_1477), mdl (edam:format_3815), mmcif (edam:format_1477), mol (edam:format_3815), mol2 (edam:format_3816), pdb (edam:format_1476), pdbqt (edam:format_1476), png (edam:format_3603), sdf (edam:format_3814), smi (edam:format_1196), smiles (edam:format_1196), txt (edam:format_2033).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **input_format** (*str*) - (None) Format of input file. If not provided, input_path extension will be taken. Values: dat (Information represented in a data record), ent (Protein Data Bank format), fa (FASTA sequence format), fasta (FASTA sequence format), gro (GROMACS structure), inp (AMBER trajectory format), log (Events file), mcif (Entry format of PDB database in mmCIF format), mdl (file format for holding information about the atoms; bonds; connectivity and coordinates of a molecule), mmcif (Entry format of PDB database in mmCIF format), mol (file format for holding information about the atoms; bonds; connectivity and coordinates of a molecule), mol2 (Complete and portable representation of a SYBYL molecule), pdb (Protein Data Bank format), pdbqt (Protein Data Bank format with charges), png (File format for image compression), sdf (One of a family of chemical-data file formats developed by MDL Information Systems), smi (Chemical structure specified in Simplified Molecular Input Line Entry System line notation.), smiles (Chemical structure specified in Simplified Molecular Input Line Entry System line notation.), txt (Textual format), xml (eXtensible Markup Language), xtc (Portable binary format for trajectories produced by GROMACS package).
            * **output_format** (*str*) - (None) Format of output file. If not provided, output_path extension will be taken. Values: ent (Protein Data Bank format), fa (FASTA sequence format), fasta (FASTA sequence format), gro (GROMACS structure), inp (AMBER trajectory format), mcif (Entry format of PDB database in mmCIF format), mdl (file format for holding information about the atoms; bonds; connectivity and coordinates of a molecule), mmcif (Entry format of PDB database in mmCIF format), mol (file format for holding information about the atoms; bonds; connectivity and coordinates of a molecule), mol2 (Complete and portable representation of a SYBYL molecule), pdb (Protein Data Bank format), pdbqt (Protein Data Bank format with charges), png (File format for image compression), sdf (One of a family of chemical-data file formats developed by MDL Information Systems), smi (Chemical structure specified in Simplified Molecular Input Line Entry System line notation.), smiles (Chemical structure specified in Simplified Molecular Input Line Entry System line notation.), txt (Textual format), xtc (Portable binary format for trajectories produced by GROMACS package).
            * **fs_input** (*list*) - (None) Format-specific input options. Values: b (disable automatic bonding), d (input file is in dlg -AutoDock docking log- format).
            * **fs_output** (*list*) - (None) Format-specific output options. Values: b (enable automatic bonding), r (output as a rigid molecule), c (combine separate molecular pieces of input into a single rigid molecule), s (output as a flexible residue), p (preserve atom indices from input file), h (preserve hydrogens), n (preserve atom names).
            * **coordinates** (*int*) - (None) Type of coordinates: 2D or 3D. Values: 2 (2D coordinates), 3 (3D coordinates).
            * **effort** (*str*) - ("medium") Computational effort wanted to dedicate for the conformer generation coordinates calculations, only for 3D coordinates. Values: fastest (only generate coordinates, no force field or conformer search), fast (perform quick forcefield optimization), medium (forcefield optimization + fast conformer search), better (more optimization + fast conformer search), best (more optimization + significant conformer search).
            * **ph** (*float*) - (7.4) [0~14|0.1] Add hydrogens appropriate for pH.
            * **flex** (*bool*) - (False) Remove all but the largest contiguous fragment (strip salts).
            * **binary_path** (*str*) - ("obabel") Path to the obabel executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.
            * **container_path** (*str*) - (None) Container path definition.
            * **container_image** (*str*) - ('informaticsmatters/obabel:latest') Container image definition.
            * **container_volume_path** (*str*) - ('/tmp') Container volume path definition.
            * **container_working_dir** (*str*) - (None) Container working directory definition.
            * **container_user_id** (*str*) - (None) Container user_id definition.
            * **container_shell_path** (*str*) - ('/bin/bash') Path to default shell inside the container.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_chemistry.babelm.babel_convert import babel_convert
            prop = {
                'input_format': 'smi',
                'output_format': 'mol2',
                'coordinates': 3,
                'ph': 7.4
            }
            babel_convert(input_path='/path/to/my2DMolecule.smi',
                        output_path='/path/to/new3DMolecule.mol2',
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

    def __init__(self, input_path, output_path, properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = {
            "in": {"input_path": input_path},
            "out": {"output_path": output_path},
        }

        # Properties specific for BB
        self.input_format = properties.get("input_format", "")
        self.output_format = properties.get("output_format", "")
        self.fs_input = _from_string_to_list(properties.get("fs_input", None))
        self.fs_output = _from_string_to_list(properties.get("fs_output", None))
        self.coordinates = properties.get("coordinates", "")
        self.effort = properties.get("effort", "medium")
        self.ph = properties.get("ph", "")
        self.flex = properties.get("flex", False)
        self.binary_path = properties.get("binary_path", "obabel")
        self.properties = properties

        # Check the properties
        self.check_properties(properties)
        self.check_arguments()

    def check_data_params(self, out_log, err_log):
        """Checks all the input/output paths and parameters"""
        self.io_dict["in"]["input_path"] = check_input_path(
            self.io_dict["in"]["input_path"], out_log, self.__class__.__name__
        )
        self.io_dict["out"]["output_path"] = check_output_path(
            self.io_dict["out"]["output_path"], out_log, self.__class__.__name__
        )

    def create_cmd(self, container_io_dict, out_log, err_log):
        """Creates the command line instruction using the properties file settings"""
        instructions_list = []

        # executable path
        instructions_list.append(self.binary_path)

        # generating input
        infr = get_input_format(
            self.input_format, container_io_dict["in"]["input_path"], out_log
        )
        iformat = "-i" + infr
        instructions_list.append(iformat)
        ipath = container_io_dict["in"]["input_path"]
        instructions_list.append(ipath)

        # generating output
        oufr = get_output_format(
            self.output_format, container_io_dict["out"]["output_path"], out_log
        )
        oformat = "-o" + oufr
        instructions_list.append(oformat)
        opath = "-O" + container_io_dict["out"]["output_path"]
        instructions_list.append(opath)

        # adding coordinates
        crd = get_coordinates(self.coordinates, out_log)
        coordinates = ""
        if crd:
            coordinates = "--gen" + crd + "d"
            instructions_list.append(coordinates)

        # adding pH
        p = get_ph(self.ph, out_log)
        ph = ""
        if p:
            ph = "-p " + p
            instructions_list.append(ph)

        # flex
        flex = ""
        if not self.flex:
            flex = "-r"
            instructions_list.append(flex)

        # fs_input
        if self.fs_input is not None:
            for fsi in self.fs_input:
                instructions_list.append("-a" + fsi)

        # fs_output
        if self.fs_output is not None:
            for fso in self.fs_output:
                instructions_list.append("-x" + fso)

        # adding effort (only for 3D coordinates)
        if crd == "3":
            instructions_list.append("--" + self.effort)

        return instructions_list

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`BabelConvert <babelm.babel_convert.BabelConvert>` babelm.babel_convert.BabelConvert object."""

        # check input/output paths and parameters
        self.check_data_params(self.out_log, self.err_log)

        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        # create command line instruction
        self.cmd = self.create_cmd(self.stage_io_dict, self.out_log, self.err_log)

        # Run Biobb block
        self.run_biobb()

        # Copy files to host
        self.copy_to_host()

        # remove temporary folder(s)
        self.tmp_files.extend([self.stage_io_dict.get("unique_dir", "")])
        self.remove_tmp_files()

        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code


def babel_convert(
    input_path: str, output_path: str, properties: Optional[dict] = None, **kwargs
) -> int:
    """Execute the :class:`BabelConvert <babelm.babel_convert.BabelConvert>` class and
    execute the :meth:`launch() <babelm.babel_convert.BabelConvert.launch>` method."""

    return BabelConvert(
        input_path=input_path, output_path=output_path, properties=properties, **kwargs
    ).launch()


def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(
        description="Small molecule format conversion.",
        formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999),
    )
    parser.add_argument("--config", required=False, help="Configuration file")

    # Specific args of each building block
    required_args = parser.add_argument_group("required arguments")
    required_args.add_argument(
        "--input_path",
        required=True,
        help="Path to the input file. Accepted formats: dat, ent, fa, fasta, gro, inp, log, mcif, mdl, mmcif, mol, mol2, pdb, pdbqt, png, sdf, smi, smiles, txt, xml, xtc.",
    )
    required_args.add_argument(
        "--output_path",
        required=True,
        help="Path to the output file. Accepted formats: ent, fa, fasta, gro, inp, mcif, mdl, mmcif, mol, mol2, pdb, pdbqt, png, sdf, smi, smiles, txt.",
    )

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    # Specific call of each building block
    babel_convert(
        input_path=args.input_path, output_path=args.output_path, properties=properties
    )


if __name__ == "__main__":
    main()
