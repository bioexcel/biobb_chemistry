#!/usr/bin/env python3

"""Module containing the AcpypeParamsGMXOPLS class and the command line interface."""
from typing import Optional
from biobb_common.generic.biobb_object import launcher
from biobb_chemistry.acpype import common


class AcpypeParamsGMXOPLS(common.AcpypeBase):
    """
    | biobb_chemistry AcpypeParamsGMXOPLS
    | This class is a wrapper of `Acpype <https://github.com/alanwilter/acpype>`_ tool for generation of topologies for OPLS/AA.
    | Generation of topologies for OPLS/AA. Acpype is a tool based in Python to use Antechamber to generate topologies for chemical compounds and to interface with others python applications like CCPN or ARIA. `Visit the official page <https://github.com/alanwilter/acpype>`_.

    Args:
        input_path (str): Path to the input file. File type: input. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/acpype/acpype.params.mol2>`_. Accepted formats: pdb (edam:format_1476), mdl (edam:format_3815), mol2 (edam:format_3816).
        output_path_itp (str): Path to the ITP output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.gmx.opls.itp>`_. Accepted formats: itp (edam:format_3883).
        output_path_top (str): Path to the TOP output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.gmx.opls.top>`_. Accepted formats: top (edam:format_3880).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **basename** (*str*) - ("BBB") A basename for the project (folder and output files).
            * **charge** (*int*) - (None) [-20~20|1] Net molecular charge, for gas default is 0. If None the charge is guessed by acpype.
            * **charge_method** (*str*) - ("bcc") Charge method. Values: gas (Gasteiger charges), bcc (AM1-BCC charges), abcg2 (ABCG2 charges; recommended for GAFF2; not available in acpype 2023.10.27), user (charges read from the mol2 input file).
            * **multiplicity** (*int*) - (1) [1~10|1] Multiplicity (2S+1) of the molecule.
            * **atom_type** (*str*) - ("gaff2") Atom type. Values: gaff (General AMBER Force Field), amber (protein force field set in protein_ff + GAFF), gaff2 (General AMBER Force Field 2), amber2 (protein force field set in protein_ff + GAFF2).
            * **protein_ff** (*str*) - ("ff14SB") Protein force field used with the amber and amber2 atom types; only written to the command line when it is not the default value, not available in acpype 2023.10.27. Values: ff14SB (AMBER ff14SB), ff99SB (AMBER ff99SB).
            * **qprog** (*str*) - ("sqm") AM1-BCC charges engine; mopac and divcon need a full external AmberTools. Values: sqm (sqm), mopac (MOPAC), divcon (DivCon).
            * **keyword** (*str*) - (None) Keyword of the mopac or sqm engine, ie: "qm_theory='AM1', grms_tol=0.0005, scfconv=1.d-10".
            * **max_time** (*int*) - (10800) [1~1000000|1] Maximum time (in seconds) for the sqm or mopac execution.
            * **predindex** (*int*) - (4) [0~5|1] Antechamber atom and bond type prediction index, the antechamber -j flag; only 1, 4 and 5 produce a topology. Only written to the command line when it is not the default value, not available in acpype 2023.10.27. Values: 0 (no prediction), 1 (atom type), 2 (full bond types), 3 (part bond types), 4 (atom and full bond type), 5 (atom and part bond type).
            * **gmx4** (*bool*) - (False) Write Ryckaert-Bellemans dihedrals for the old GROMACS 4.0.
            * **merge** (*bool*) - (False) Merge lower and uppercase atom types in the GROMACS topology if their parameters match.
            * **sorted** (*bool*) - (False) Sort atoms for the GROMACS ordering.
            * **binary_path** (*str*) - ("acpype") Path to the acpype executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.
            * **container_path** (*str*) - (None) Container path definition.
            * **container_image** (*str*) - ('acpype/acpype:2022.7.21') Container image definition.
            * **container_volume_path** (*str*) - ('/tmp') Container volume path definition.
            * **container_user_id** (*str*) - (None) Container user_id definition.
            * **container_shell_path** (*str*) - ('/bin/bash') Path to default shell inside the container.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_chemistry.acpype.acpype_params_gmx_opls import acpype_params_gmx_opls
            prop = {
                'basename': 'BBB',
                'charge': 0
            }
            acpype_params_gmx_opls(input_path='/path/to/myStructure.mol2',
                                    output_path_itp='/path/to/newITP.itp',
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

    acpype_options = common.PARAMS_OPTIONS + common.GMX_OPTIONS
    acpype_outputs = {'output_path_itp': '_GMX_OPLS.itp', 'output_path_top': '_GMX_OPLS.top'}
    # acpype includes BBB_GMX.itp in the OPLS/AA top
    acpype_includes = {'output_path_top': {'_GMX.itp': 'output_path_itp'}}

    def __init__(self, input_path: str, output_path_itp: str, output_path_top: str,
                 properties: Optional[dict] = None, **kwargs) -> None:
        super().__init__(**locals())


acpype_params_gmx_opls = launcher(AcpypeParamsGMXOPLS)

if __name__ == '__main__':
    AcpypeParamsGMXOPLS.main()
