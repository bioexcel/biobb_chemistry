#!/usr/bin/env python3

"""Module containing the Open Babel class and the command line interface."""
import argparse
from biobb_common.configuration import  settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from biobb_common.command_wrapper import cmd_wrapper
from biobb_chemistry.babelm.common import *

class BabelConvert():
    """Small molecule format conversion.
    Wrapper for the Open Babel module. Format conversion for structures or trajectories.
    Open Babel is a chemical toolbox designed to speak the many languages of chemical data. It's an open, collaborative project 
    allowing anyone to search, convert, analyze, or store data from molecular modeling, chemistry, solid-state materials, 
    biochemistry, or related areas. `Visit the official page <http://openbabel.org/wiki/Main_Page>`_.

    Args:
        input_path (str): Path to the input file. File type: input. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/babel/babel.smi>`_. Accepted formats: abinit, acesout, acr, adfout, alc, aoforce, arc, axsf, bgf, box, bs, c09out, c3d2, caccrt, can, car, castep, ccc, cdjson, cdx, cdxml, cif, ck, cml, cmlr, CONFIG, CONTCAR, CONTFF, crk2d, crk3d, ct, cub, cube, dallog, dalmol, dat, dmol, dx, ent, exyz, fa, fasta, fch, fchk, fck, feat, fhiaims, fract, fs, fsa, g03, g09, g92, g94, g98, gal, gam, gamess, gamin, gamout, got, gpr, gro, gukin, gukout, gzmat, hin, HISTORY, inchi, inp, ins, jin, jout, log, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mol, mol2, mold, molden, molf, moo, mop, mopcrt, mopin, mopout, mpc, mpo, mpqc, mrv, msi, nwo, orca, out, outmol, output, pc, pcjson, pcm, pdb, pdbqt, png, pos, POSCAR, POSFF, pqr, pqs, prep, pwscf, qcout, res, rsmi, rxn, sd, sdf, siesta, smi, smiles, smy, sy2, t41, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xml, xsf, xtc, xyz, yob.
        output_path (str): Path to the output file. File type: output. `Sample file <https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/babel/ref_babel.convert.mol2>`_. Accepted formats: acesin, adf, alc, ascii, bgf, box, bs, c3d1, c3d2, cac, caccrt, cache, cacint, can, cdjson, cdxml, cht, cif, ck, cml, cmlr, com, confabreport, CONFIG, CONTCAR, CONTFF, copy, crk2d, crk3d, csr, cssr, ct, cub, cube, dalmol, dmol, dx, ent, exyz, fa, fasta, feat, fh, fhiaims, fix, fps, fpt, fract, fs, fsa, gamin, gau, gjc, gjf, gpr, gr96, gro, gukin, gukout, gzmat, hin, inchi, inchikey, inp, jin, k, lmpdat, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mna, mol, mol2, mold, molden, molf, molreport, mop, mopcrt, mopin, mp, mpc, mpd, mpqcin, mrv, msms, nul, nw, orcainp, outmol, paint, pcjson, pcm, pdb, pdbqt, png, pointcloud, POSCAR, POSFF, pov, pqr, pqs, qcin, report, rsmi, rxn, sd, sdf, smi, smiles, stl, svg, sy2, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xed, xyz, yob, zin.
        properties (dic):
            * **input_format** (*str*) - (None) Format of input file. If not provided, file extension will be taken. Values: abinit, acesout, acr, adfout, alc, aoforce, arc, axsf, bgf, box, bs, c09out, c3d2, caccrt, can, car, castep, ccc, cdjson, cdx, cdxml, cif, ck, cml, cmlr, CONFIG, CONTCAR, CONTFF, crk2d, crk3d, ct, cub, cube, dallog, dalmol, dat, dmol, dx, ent, exyz, fa, fasta, fch, fchk, fck, feat, fhiaims, fract, fs, fsa, g03, g09, g92, g94, g98, gal, gam, gamess, gamin, gamout, got, gpr, gro, gukin, gukout, gzmat, hin, HISTORY, inchi, inp, ins, jin, jout, log, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mol, mol2, mold, molden, molf, moo, mop, mopcrt, mopin, mopout, mpc, mpo, mpqc, mrv, msi, nwo, orca, out, outmol, output, pc, pcjson, pcm, pdb, pdbqt, png, pos, POSCAR, POSFF, pqr, pqs, prep, pwscf, qcout, res, rsmi, rxn, sd, sdf, siesta, smi, smiles, smy, sy2, t41, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xml, xsf, xtc, xyz, yob.
            * **output_format** (*str*) - (None) Format of output file. If not provided, file extension will be taken. Values: acesin, adf, alc, ascii, bgf, box, bs, c3d1, c3d2, cac, caccrt, cache, cacint, can, cdjson, cdxml, cht, cif, ck, cml, cmlr, com, confabreport, CONFIG, CONTCAR, CONTFF, copy, crk2d, crk3d, csr, cssr, ct, cub, cube, dalmol, dmol, dx, ent, exyz, fa, fasta, feat, fh, fhiaims, fix, fps, fpt, fract, fs, fsa, gamin, gau, gjc, gjf, gpr, gr96, gro, gukin, gukout, gzmat, hin, inchi, inchikey, inp, jin, k, lmpdat, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mna, mol, mol2, mold, molden, molf, molreport, mop, mopcrt, mopin, mp, mpc, mpd, mpqcin, mrv, msms, nul, nw, orcainp, outmol, paint, pcjson, pcm, pdb, pdbqt, png, pointcloud, POSCAR, POSFF, pov, pqr, pqs, qcin, report, rsmi, rxn, sd, sdf, smi, smiles, stl, svg, sy2, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xed, xyz, yob, zin.
            * **coordinates** (*int*) - (None) Type of coordinates: 2D or 3D. Values: 2, 3.
            * **ph** (*float*) - (None) Add hydrogens appropriate for pH.
            * **obabel_path** (*str*) - ("obabel") Path to the obabel executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **container_path** (*str*) - (None) Container path definition.
            * **container_image** (*str*) - ('informaticsmatters/obabel:latest') Container image definition.
            * **container_volume_path** (*str*) - ('/tmp') Container volume path definition.
            * **container_working_dir** (*str*) - (None) Container working directory definition.
            * **container_user_id** (*str*) - (None) Container user_id definition.
            * **container_shell_path** (*str*) - ('/bin/bash') Path to default shell inside the container.
    """

    def __init__(self, input_path, output_path, properties=None, **kwargs):
        properties = properties or {}

        # Input/Output files
        self.io_dict = { 
            "in": { "input_path": check_input_path(input_path, self.__class__.__name__) }, 
            "out": { "output_path": check_output_path(output_path, self.__class__.__name__) } 
        }

        # Properties specific for BB
        self.input_format = properties.get('input_format', '')
        self.output_format = properties.get('output_format', '')
        self.coordinates = properties.get('coordinates', '')
        self.ph = properties.get('ph', '')
        self.obabel_path = get_binary_path(properties, 'obabel_path')
        self.properties = properties

        # container Specific
        self.container_path = properties.get('container_path')
        self.container_image = properties.get('container_image', 'informaticsmatters/obabel:latest')
        self.container_volume_path = properties.get('container_volume_path', '/tmp')
        self.container_working_dir = properties.get('container_working_dir')
        self.container_user_id = properties.get('container_user_id')
        self.container_shell_path = properties.get('container_shell_path', '/bin/bash')

        # Properties common in all BB
        self.can_write_console_log = properties.get('can_write_console_log', True)
        self.global_log = properties.get('global_log', None)
        self.prefix = properties.get('prefix', None)
        self.step = properties.get('step', None)
        self.path = properties.get('path', '')
        self.remove_tmp = properties.get('remove_tmp', True)
        self.restart = properties.get('restart', False)

    def create_cmd(self, container_io_dict, out_log, err_log):
        """Creates the command line instruction using the properties file settings"""
        instructions_list = []

        # executable path
        instructions_list.append(self.obabel_path)

        # generating input 
        infr = get_input_format(self.input_format, container_io_dict["in"]["input_path"], out_log)
        iformat = '-i' + infr
        instructions_list.append(iformat)
        ipath = container_io_dict["in"]["input_path"]
        instructions_list.append(ipath)

        # generating output 
        oufr = get_output_format(self.output_format, container_io_dict["out"]["output_path"], out_log)
        oformat = '-o' + oufr
        instructions_list.append(oformat)
        opath = '-O' + container_io_dict["out"]["output_path"]
        instructions_list.append(opath)

        # adding coordinates
        crd = get_coordinates(self.coordinates, out_log)
        coordinates = ''
        if crd:
            coordinates = '--gen' + crd + 'd'

        instructions_list.append(coordinates)

        # adding pH
        p = get_ph(self.ph, out_log)
        ph = ''
        if p:
            ph = '-p ' + p

        instructions_list.append(ph)

        return instructions_list

    @launchlogger
    def launch(self):
        """Launches the execution of the Open Babel module."""
        
        # Get local loggers from launchlogger decorator
        out_log = getattr(self, 'out_log', None)
        err_log = getattr(self, 'err_log', None)

        # Check the properties
        fu.check_properties(self, self.properties)

        if self.restart:
            output_file_list = [self.io_dict["out"]["output_path"]]
            if fu.check_complete_files(output_file_list):
                fu.log('Restart is enabled, this step: %s will the skipped' % self.step, out_log, self.global_log)
                return 0

        # copy inputs to container
        container_io_dict = fu.copy_to_container(self.container_path, self.container_volume_path, self.io_dict)

        # create and execute command line instruction
        cmd = self.create_cmd(container_io_dict, out_log, err_log) 
        cmd = fu.create_cmd_line(cmd, container_path=self.container_path, 
                                 host_volume=container_io_dict.get("unique_dir"), 
                                 container_volume=self.container_volume_path, 
                                 container_working_dir=self.container_working_dir, 
                                 container_user_uid=self.container_user_id, 
                                 container_image=self.container_image, 
                                 container_shell_path=self.container_shell_path, 
                                 out_log=out_log, global_log=self.global_log)
        returncode = cmd_wrapper.CmdWrapper(cmd, out_log, err_log, self.global_log).launch()

        # copy output(s) to output(s) path(s) in case of container execution
        fu.copy_to_host(self.container_path, container_io_dict, self.io_dict)

        # remove temporary folder(s)
        if self.container_path and self.remove_tmp: 
            fu.rm(container_io_dict['unique_dir'])
            fu.log('Removed: %s' % str(container_io_dict['unique_dir']), out_log)

        return returncode

def main():
    parser = argparse.ArgumentParser(description="Small molecule format conversion.", formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')

    # Specific args of each building block
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_path', required=True, help='Path to the input file. Accepted formats: abinit, acesout, acr, adfout, alc, aoforce, arc, axsf, bgf, box, bs, c09out, c3d2, caccrt, can, car, castep, ccc, cdjson, cdx, cdxml, cif, ck, cml, cmlr, CONFIG, CONTCAR, CONTFF, crk2d, crk3d, ct, cub, cube, dallog, dalmol, dat, dmol, dx, ent, exyz, fa, fasta, fch, fchk, fck, feat, fhiaims, fract, fs, fsa, g03, g09, g92, g94, g98, gal, gam, gamess, gamin, gamout, got, gpr, gro, gukin, gukout, gzmat, hin, HISTORY, inchi, inp, ins, jin, jout, log, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mol, mol2, mold, molden, molf, moo, mop, mopcrt, mopin, mopout, mpc, mpo, mpqc, mrv, msi, nwo, orca, out, outmol, output, pc, pcjson, pcm, pdb, pdbqt, png, pos, POSCAR, POSFF, pqr, pqs, prep, pwscf, qcout, res, rsmi, rxn, sd, sdf, siesta, smi, smiles, smy, sy2, t41, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xml, xsf, xtc, xyz, yob.')
    required_args.add_argument('--output_path', required=True, help='Path to the output file. Accepted formats: acesin, adf, alc, ascii, bgf, box, bs, c3d1, c3d2, cac, caccrt, cache, cacint, can, cdjson, cdxml, cht, cif, ck, cml, cmlr, com, confabreport, CONFIG, CONTCAR, CONTFF, copy, crk2d, crk3d, csr, cssr, ct, cub, cube, dalmol, dmol, dx, ent, exyz, fa, fasta, feat, fh, fhiaims, fix, fps, fpt, fract, fs, fsa, gamin, gau, gjc, gjf, gpr, gr96, gro, gukin, gukout, gzmat, hin, inchi, inchikey, inp, jin, k, lmpdat, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mna, mol, mol2, mold, molden, molf, molreport, mop, mopcrt, mopin, mp, mpc, mpd, mpqcin, mrv, msms, nul, nw, orcainp, outmol, paint, pcjson, pcm, pdb, pdbqt, png, pointcloud, POSCAR, POSFF, pov, pqr, pqs, qcin, report, rsmi, rxn, sd, sdf, smi, smiles, stl, svg, sy2, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xed, xyz, yob, zin.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    # Specific call of each building block
    BabelConvert(input_path=args.input_path, output_path=args.output_path, 
                 properties=properties).launch()

if __name__ == '__main__':
    main()
