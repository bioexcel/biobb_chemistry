#!/usr/bin/env python3

"""Module containing the BabelMinimize class and the command line interface."""
from typing import Optional
from pathlib import PurePath
from biobb_common.generic.biobb_object import BiobbObject, launcher
from biobb_common.tools import file_utils as fu
from biobb_chemistry.babelm.common import MINIMIZE_OPTIONS, is_valid_minimize_value


class BabelMinimize(BiobbObject):
    """
    | biobb_chemistry BabelMinimize
    | This class is a wrapper of the Open Babel tool.
    | Energetically minimizes small molecules. Open Babel is a chemical toolbox designed to speak the many languages of chemical data. It's an open, collaborative project allowing anyone to search, convert, analyze, or store data from molecular modeling, chemistry, solid-state materials, biochemistry, or related areas. `Visit the official page <http://openbabel.org/wiki/Main_Page>`_.

    Args:
        input_path (str): Path to the input file. File type: input. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/babelm/babel.minimize.pdb>`_. Accepted formats: pdb (edam:format_1476), mol2 (edam:format_3816).
        output_path (str): Path to the output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/babelm/ref_babel.minimize.pdb>`_. Accepted formats: pdb (edam:format_1476), mol2 (edam:format_3816).
        properties (dic - Python dictionary object containing the tool parameters, not input/output files):
            * **criteria** (*float*) - (None) Convergence criteria. If not set, obminimize uses its own default.
            * **method** (*str*) - (None) Method. If not set, obminimize uses its own default. Values: cg (conjugate gradients algorithm), sd (steepest descent algorithm).
            * **force_field** (*str*) - (None) Force field. If not set, obminimize uses its own default. Values: GAFF (General Amber Force Field), Ghemical (Ghemical force field), MMFF94 (MMFF94 force field), MMFF94s (MMFF94s force field), UFF (Universal Force Field).
            * **hydrogens** (*bool*) - (None) Add hydrogen atoms. If not set, obminimize uses its own default.
            * **steps** (*int*) - (None) [0~5000|1] Maximum number of steps. If not set, obminimize uses its own default.
            * **cutoff** (*bool*) - (None) Use cut-off. If not set, obminimize uses its own default.
            * **rvdw** (*float*) - (None) [0~50|1.0] VDW cut-off distance. If not set, obminimize uses its own default.
            * **rele** (*float*) - (None) [0~50|1.0] Electrostatic cut-off distance. If not set, obminimize uses its own default.
            * **frequency** (*int*) - (None) [0~50|1] Frequency to update the non-bonded pairs. If not set, obminimize uses its own default.
            * **binary_path** (*str*) - ("obminimize") Path to the obminimize executable binary.
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

    def __init__(self, input_path: str, output_path: str,
                 properties: Optional[dict] = None, **kwargs) -> None:
        super().__init__(**locals())

    def prepare(self) -> None:
        """Leaves out the options with a value that is not valid: obminimize uses its own default"""
        for name, (flag, kind) in MINIMIZE_OPTIONS.items():
            value = getattr(self, name)
            if value is not None and str(value) != "" and not is_valid_minimize_value(value, kind):
                fu.log("Value %s of the %s property is not valid, obminimize default used" % (value, name), self.out_log)
                setattr(self, name, None)

    def create_cmd(self, container_io_dict, out_log, err_log):
        """Creates the command line instruction using the properties file settings"""
        instructions_list = [self.binary_path]

        for name, (flag, kind) in MINIMIZE_OPTIONS.items():
            value = getattr(self, name)
            if value is None or str(value) == "" or (kind is bool and str(value) == "False"):
                continue
            instructions_list.append(flag.format(value))

        iextension = PurePath(container_io_dict["in"]["input_path"]).suffix
        oextension = PurePath(container_io_dict["out"]["output_path"]).suffix

        instructions_list.append('-i' + iextension[1:] + ' ' + container_io_dict["in"]["input_path"])

        instructions_list.append('-o' + oextension[1:])

        instructions_list.append('>')

        instructions_list.append(container_io_dict["out"]["output_path"])

        return instructions_list

    def run(self) -> None:
        """Execute the :class:`BabelMinimize <babelm.babel_minimize.BabelMinimize>` babelm.babel_minimize.BabelMinimize object."""

        # create command line instruction
        self.cmd = self.create_cmd(self.stage_io_dict, self.out_log, self.err_log)

        # Run Biobb block
        self.run_biobb()


babel_minimize = launcher(BabelMinimize)


if __name__ == '__main__':
    BabelMinimize.main()
