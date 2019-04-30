
BioBB Chemistry Command Line Help
=================================

Generic usage:

.. parsed-literal::

    biobb_command [-h] --config CONFIG [--system SYSTEM] [--step STEP] --input_file(s) <input_file(s)> --output_file <output_file>

Please refer to the `system & step
documentation <https://biobb-common.readthedocs.io/en/latest/system_step.html>`__
for more information of these two parameters.

--------------

Babel convert
-------------

Wrapper for the Open Babel module. Format conversion for structures or
trajectories.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    babel_convert -h

.. parsed-literal::

    usage: babel_convert [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_path INPUT_PATH --output_path OUTPUT_PATH
    
    Wrapper for the Open Babel module. Format conversion for structures or trajectories.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_path INPUT_PATH
                            Path to the input file. Accepted formats: abinit, acesout, acr, adfout, alc, aoforce, arc, axsf, bgf, box, bs, c09out, c3d2, caccrt, can, car, castep, ccc, cdjson, cdx, cdxml, cif, ck, cml, cmlr, CONFIG, CONTCAR, CONTFF, crk2d, crk3d, ct, cub, cube, dallog, dalmol, dat, dmol, dx, ent, exyz, fa, fasta, fch, fchk, fck, feat, fhiaims, fract, fs, fsa, g03, g09, g92, g94, g98, gal, gam, gamess, gamin, gamout, got, gpr, gro, gukin, gukout, gzmat, hin, HISTORY, inchi, inp, ins, jin, jout, log, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mol, mol2, mold, molden, molf, moo, mop, mopcrt, mopin, mopout, mpc, mpo, mpqc, mrv, msi, nwo, orca, out, outmol, output, pc, pcjson, pcm, pdb, pdbqt, png, pos, POSCAR, POSFF, pqr, pqs, prep, pwscf, qcout, res, rsmi, rxn, sd, sdf, siesta, smi, smiles, smy, sy2, t41, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xml, xsf, xtc, xyz, yob.
      --output_path OUTPUT_PATH
                            Path to the output file. Accepted formats: acesin, adf, alc, ascii, bgf, box, bs, c3d1, c3d2, cac, caccrt, cache, cacint, can, cdjson, cdxml, cht, cif, ck, cml, cmlr, com, confabreport, CONFIG, CONTCAR, CONTFF, copy, crk2d, crk3d, csr, cssr, ct, cub, cube, dalmol, dmol, dx, ent, exyz, fa, fasta, feat, fh, fhiaims, fix, fps, fpt, fract, fs, fsa, gamin, gau, gjc, gjf, gpr, gr96, gro, gukin, gukout, gzmat, hin, inchi, inchikey, inp, jin, k, lmpdat, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mna, mol, mol2, mold, molden, molf, molreport, mop, mopcrt, mopin, mp, mpc, mpd, mpqcin, mrv, msms, nul, nw, orcainp, outmol, paint, pcjson, pcm, pdb, pdbqt, png, pointcloud, POSCAR, POSFF, pov, pqr, pqs, qcin, report, rsmi, rxn, sd, sdf, smi, smiles, stl, svg, sy2, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xed, xyz, yob, zin.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input\_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input\_path** (*str*): Path to the input file. Accepted formats:
   abinit, acesout, acr, adfout, alc, aoforce, arc, axsf, bgf, box, bs,
   c09out, c3d2, caccrt, can, car, castep, ccc, cdjson, cdx, cdxml, cif,
   ck, cml, cmlr, CONFIG, CONTCAR, CONTFF, crk2d, crk3d, ct, cub, cube,
   dallog, dalmol, dat, dmol, dx, ent, exyz, fa, fasta, fch, fchk, fck,
   feat, fhiaims, fract, fs, fsa, g03, g09, g92, g94, g98, gal, gam,
   gamess, gamin, gamout, got, gpr, gro, gukin, gukout, gzmat, hin,
   HISTORY, inchi, inp, ins, jin, jout, log, lpmd, mcdl, mcif, MDFF,
   mdl, ml2, mmcif, mmd, mmod, mol, mol2, mold, molden, molf, moo, mop,
   mopcrt, mopin, mopout, mpc, mpo, mpqc, mrv, msi, nwo, orca, out,
   outmol, output, pc, pcjson, pcm, pdb, pdbqt, png, pos, POSCAR, POSFF,
   pqr, pqs, prep, pwscf, qcout, res, rsmi, rxn, sd, sdf, siesta, smi,
   smiles, smy, sy2, t41, tdd, text, therm, tmol, txt, txyz, unixyz,
   VASP, vmol, xml, xsf, xtc, xyz, yob.
-  **output\_path** (*str*): Path to the output file. Accepted formats:
   acesin, adf, alc, ascii, bgf, box, bs, c3d1, c3d2, cac, caccrt,
   cache, cacint, can, cdjson, cdxml, cht, cif, ck, cml, cmlr, com,
   confabreport, CONFIG, CONTCAR, CONTFF, copy, crk2d, crk3d, csr, cssr,
   ct, cub, cube, dalmol, dmol, dx, ent, exyz, fa, fasta, feat, fh,
   fhiaims, fix, fps, fpt, fract, fs, fsa, gamin, gau, gjc, gjf, gpr,
   gr96, gro, gukin, gukout, gzmat, hin, inchi, inchikey, inp, jin, k,
   lmpdat, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mna, mol,
   mol2, mold, molden, molf, molreport, mop, mopcrt, mopin, mp, mpc,
   mpd, mpqcin, mrv, msms, nul, nw, orcainp, outmol, paint, pcjson, pcm,
   pdb, pdbqt, png, pointcloud, POSCAR, POSFF, pov, pqr, pqs, qcin,
   report, rsmi, rxn, sd, sdf, smi, smiles, stl, svg, sy2, tdd, text,
   therm, tmol, txt, txyz, unixyz, VASP, vmol, xed, xyz, yob, zin.

Config
~~~~~~

Syntax: input\_parameter (datatype) - (default\_value) Definition

Config parameters for this building block:

-  **input\_format** (*str*) - (None) Format of input file. If not
   provided, file extension will be taken. Values: abinit, acesout, acr,
   adfout, alc, aoforce, arc, axsf, bgf, box, bs, c09out, c3d2, caccrt,
   can, car, castep, ccc, cdjson, cdx, cdxml, cif, ck, cml, cmlr,
   CONFIG, CONTCAR, CONTFF, crk2d, crk3d, ct, cub, cube, dallog, dalmol,
   dat, dmol, dx, ent, exyz, fa, fasta, fch, fchk, fck, feat, fhiaims,
   fract, fs, fsa, g03, g09, g92, g94, g98, gal, gam, gamess, gamin,
   gamout, got, gpr, gro, gukin, gukout, gzmat, hin, HISTORY, inchi,
   inp, ins, jin, jout, log, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif,
   mmd, mmod, mol, mol2, mold, molden, molf, moo, mop, mopcrt, mopin,
   mopout, mpc, mpo, mpqc, mrv, msi, nwo, orca, out, outmol, output, pc,
   pcjson, pcm, pdb, pdbqt, png, pos, POSCAR, POSFF, pqr, pqs, prep,
   pwscf, qcout, res, rsmi, rxn, sd, sdf, siesta, smi, smiles, smy, sy2,
   t41, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xml, xsf,
   xtc, xyz, yob.
-  **output\_format** (*str*) - (None) Format of output file. If not
   provided, file extension will be taken. Values: acesin, adf, alc,
   ascii, bgf, box, bs, c3d1, c3d2, cac, caccrt, cache, cacint, can,
   cdjson, cdxml, cht, cif, ck, cml, cmlr, com, confabreport, CONFIG,
   CONTCAR, CONTFF, copy, crk2d, crk3d, csr, cssr, ct, cub, cube,
   dalmol, dmol, dx, ent, exyz, fa, fasta, feat, fh, fhiaims, fix, fps,
   fpt, fract, fs, fsa, gamin, gau, gjc, gjf, gpr, gr96, gro, gukin,
   gukout, gzmat, hin, inchi, inchikey, inp, jin, k, lmpdat, lpmd, mcdl,
   mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mna, mol, mol2, mold, molden,
   molf, molreport, mop, mopcrt, mopin, mp, mpc, mpd, mpqcin, mrv, msms,
   nul, nw, orcainp, outmol, paint, pcjson, pcm, pdb, pdbqt, png,
   pointcloud, POSCAR, POSFF, pov, pqr, pqs, qcin, report, rsmi, rxn,
   sd, sdf, smi, smiles, stl, svg, sy2, tdd, text, therm, tmol, txt,
   txyz, unixyz, VASP, vmol, xed, xyz, yob, zin.
-  **coordinates** (*int*) - (None) Type of coordinates: 2D or 3D.
   Values: 2, 3.
-  **ph** (*float*) - (None) Add hydrogens appropriate for pH.
-  **obabel\_path** (*str*) - ("obabel") Path to the obabel executable
   binary.

YAML file config
~~~~~~~~~~~~~~~~

average.yml:

.. parsed-literal::

    properties:
      input_format: smi
      output_format: pdb
      coordinates: 2
      ph: 7.4

Command:

.. parsed-literal::

    babel_convert --config data/conf/convert.yml --input_path data/input/babel.smi --output_path data/output/output.pdb

JSON file config
~~~~~~~~~~~~~~~~

average.json:

.. parsed-literal::

    {
      "properties": {
        "input_format": "smi",
        "output_format": "pdb",
        "coordinates": 2,
        "ph": 7.4
      }
    }

Command:

.. parsed-literal::

    babel_convert --config data/conf/convert.json --input_path data/input/babel.smi --output_path data/output/output.pdb

