#!/usr/bin/env python3

"""Module containing the BabelConvert class and the command line interface."""
from typing import Optional
from biobb_common.generic.biobb_object import launcher
from biobb_chemistry.babelm import common


class BabelConvert(common.BabelBase):
    """
    | biobb_chemistry BabelConvert
    | This class is a wrapper of the Open Babel tool.
    | Small molecule format conversion for structures or trajectories. Open Babel is a chemical toolbox designed to speak the many languages of chemical data. It's an open, collaborative project allowing anyone to search, convert, analyze, or store data from molecular modeling, chemistry, solid-state materials, biochemistry, or related areas. `Visit the official page <http://openbabel.org/wiki/Main_Page>`_.

    Args:
        input_path (str): Path to the input file. File type: input. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/babelm/babel.smi>`_. Accepted formats: dat (edam:format_1637), ent (edam:format_1476), fa (edam:format_1929), fasta (edam:format_1929), gro (edam:format_2033), inp (edam:format_3878), log (edam:format_2030), mcif (edam:format_1477), mdl (edam:format_3815), mmcif (edam:format_1477), mol (edam:format_3815), mol2 (edam:format_3816), pdb (edam:format_1476), pdbqt (edam:format_1476), png (edam:format_3603), sdf (edam:format_3814), smi (edam:format_1196), smiles (edam:format_1196), txt (edam:format_2033), xml (edam:format_2332), xtc (edam:format_3875).
        output_path (str): Path to the output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/babelm/ref_babel.convert.mol2>`_. Accepted formats: ent (edam:format_1476), fa (edam:format_1929), fasta (edam:format_1929), gro (edam:format_2033), inp (edam:format_3878), mcif (edam:format_1477), mdl (edam:format_3815), mmcif (edam:format_1477), mol (edam:format_3815), mol2 (edam:format_3816), pdb (edam:format_1476), pdbqt (edam:format_1476), png (edam:format_3603), sdf (edam:format_3814), smi (edam:format_1196), smiles (edam:format_1196), txt (edam:format_2033), dat (edam:format_1637), log (edam:format_2330), xml (edam:format_2332), xtc (edam:format_3875).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **input_format** (*str*) - (None) Format of input file. If not provided, input_path extension will be taken. Values: dat (Information represented in a data record), ent (Protein Data Bank format), fa (FASTA sequence format), fasta (FASTA sequence format), gro (GROMACS structure), inp (AMBER trajectory format), log (Events file), mcif (Entry format of PDB database in mmCIF format), mdl (file format for holding information about the atoms; bonds; connectivity and coordinates of a molecule), mmcif (Entry format of PDB database in mmCIF format), mol (file format for holding information about the atoms; bonds; connectivity and coordinates of a molecule), mol2 (Complete and portable representation of a SYBYL molecule), pdb (Protein Data Bank format), pdbqt (Protein Data Bank format with charges), png (File format for image compression), sdf (One of a family of chemical-data file formats developed by MDL Information Systems), smi (Chemical structure specified in Simplified Molecular Input Line Entry System line notation.), smiles (Chemical structure specified in Simplified Molecular Input Line Entry System line notation.), txt (Textual format), xml (eXtensible Markup Language), xtc (Portable binary format for trajectories produced by GROMACS package).
            * **output_format** (*str*) - (None) Format of output file. If not provided, output_path extension will be taken. Values: ent (Protein Data Bank format), fa (FASTA sequence format), fasta (FASTA sequence format), gro (GROMACS structure), inp (AMBER trajectory format), mcif (Entry format of PDB database in mmCIF format), mdl (file format for holding information about the atoms; bonds; connectivity and coordinates of a molecule), mmcif (Entry format of PDB database in mmCIF format), mol (file format for holding information about the atoms; bonds; connectivity and coordinates of a molecule), mol2 (Complete and portable representation of a SYBYL molecule), pdb (Protein Data Bank format), pdbqt (Protein Data Bank format with charges), png (File format for image compression), sdf (One of a family of chemical-data file formats developed by MDL Information Systems), smi (Chemical structure specified in Simplified Molecular Input Line Entry System line notation.), smiles (Chemical structure specified in Simplified Molecular Input Line Entry System line notation.), txt (Textual format), xtc (Portable binary format for trajectories produced by GROMACS package).
            * **fs_input** (*list*) - (None) Format-specific input options. Values: b (disable automatic bonding), d (input file is in dlg -AutoDock docking log- format).
            * **fs_output** (*list*) - (None) Format-specific output options. Values: b (enable automatic bonding), r (output as a rigid molecule), c (combine separate molecular pieces of input into a single rigid molecule), s (output as a flexible residue), p (preserve atom indices from input file), h (preserve hydrogens), n (preserve atom names).
            * **coordinates** (*int*) - (None) Type of coordinates: 2D or 3D. Values: 2 (2D coordinates), 3 (3D coordinates).
            * **effort** (*str*) - ("medium") Computational effort wanted to dedicate for the conformer generation coordinates calculations, only for 3D coordinates. Values: fastest (only generate coordinates, no force field or conformer search), fast (perform quick forcefield optimization), medium (forcefield optimization + fast conformer search), better (more optimization + fast conformer search), best (more optimization + significant conformer search).
            * **ph** (*float*) - (None) [0~14|0.1] Add hydrogens appropriate for pH.
            * **flex** (*bool*) - (False) Remove all but the largest contiguous fragment (strip salts).
            * **binary_path** (*str*) - ("obabel") Path to the obabel executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.
            * **container_path** (*str*) - (None) Container path definition.
            * **container_image** (*str*) - ('informaticsmatters/obabel:latest') Container image definition.
            * **container_volume_path** (*str*) - ('/tmp') Container volume path definition.
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

    def __init__(self, input_path: str, output_path: str, properties: Optional[dict] = None, **kwargs) -> None:
        super().__init__(**locals())

    def obabel_flags(self) -> list[str]:
        """Goes from the pH and flex properties to the -p and -r (strip salts) flags"""
        return (["-p " + str(self.ph)] if self.ph is not None else []) + ([] if self.flex else ["-r"])


babel_convert = launcher(BabelConvert)


if __name__ == "__main__":
    BabelConvert.main()
