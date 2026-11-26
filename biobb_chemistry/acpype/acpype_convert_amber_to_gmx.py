#!/usr/bin/env python3

"""Module containing the AcpypeConvertAMBERtoGMX class and the command line interface."""
from typing import Optional
from biobb_common.generic.biobb_object import launcher
from biobb_chemistry.acpype import common


class AcpypeConvertAMBERtoGMX(common.AcpypeBase):
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

    acpype_inputs = {'input_crd_path': '-x', 'input_top_path': '-p'}
    acpype_options = common.AMB2GMX_OPTIONS
    acpype_outputs = {'output_path_gro': '_GMX.gro', 'output_path_top': '_GMX.top'}
    acpype_folder = '.amb2gmx'

    def __init__(self, input_crd_path: str, input_top_path: str, output_path_gro: str, output_path_top: str,
                 properties: Optional[dict] = None, **kwargs) -> None:
        super().__init__(**locals())


acpype_convert_amber_to_gmx = launcher(AcpypeConvertAMBERtoGMX)

if __name__ == '__main__':
    AcpypeConvertAMBERtoGMX.main()
