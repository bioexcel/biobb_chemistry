
BioBB Chemistry Command Line Help
=================================

Generic usage:

.. parsed-literal::

    biobb_command [-h] --config CONFIG [--system SYSTEM] [--step STEP] --input_file(s) <input_file(s)> --output_file <output_file>

Please refer to the `system & step
documentation <https://biobb-common.readthedocs.io/en/latest/system_step.html>`__
for more information of these two parameters.

--------------

Acpype params AC
----------------

Wrapper for the Acpype module. Generation of topologies for Antechamber.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    acpype_params_ac -h

.. parsed-literal::

    usage: acpype_params_ac [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_path INPUT_PATH --output_path_frcmod OUTPUT_PATH_FRCMOD --output_path_inpcrd OUTPUT_PATH_INPCRD --output_path_lib OUTPUT_PATH_LIB --output_path_prmtop OUTPUT_PATH_PRMTOP
    
    Wrapper for the Acpype module. Generation of topologies for Antechamber.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_path INPUT_PATH
                            Path to the input file. Accepted formats: pdb, mdl, mol2.
      --output_path_frcmod OUTPUT_PATH_FRCMOD
                            Path to the FRCMOD output file. Accepted format: frcmod.
      --output_path_inpcrd OUTPUT_PATH_INPCRD
                            Path to the INPCRD output file. Accepted format: inpcrd.
      --output_path_lib OUTPUT_PATH_LIB
                            Path to the LIB output file. Accepted format: lib.
      --output_path_prmtop OUTPUT_PATH_PRMTOP
                            Path to the PRMTOP output file. Accepted format: prmtop.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_path** (*str*): Path to the input file. Accepted formats:
   pdb, mdl, mol2.
-  **output_path_frcmod** (*str*): Path to the FRCMOD output file.
   Accepted format: frcmod.
-  **output_path_inpcrd** (*str*): Path to the INPCRD output file.
   Accepted format: inpcrd.
-  **output_path_lib** (*str*): Path to the LIB output file. Accepted
   format: lib.
-  **output_path_prmtop** (*str*): Path to the PRMTOP output file.
   Accepted format: prmtop.

Config
~~~~~~

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **basename** (*str*) - (“BBB”) A basename for the project (folder and
   output files).
-  **charge** (*int*) - (0) Net molecular charge, for gas default is 0.
-  **acpype_path** (*str*) - (“acpype”) Path to the acpype executable
   binary.

YAML file config
~~~~~~~~~~~~~~~~

ac.yml:

.. parsed-literal::

    properties:
      basename: "BBB"
      charge: 0

Command:

.. parsed-literal::

    acpype_params_ac --config data/conf/ac.yml --input_path data/input/acpype.params.mol2 --output_path_frcmod data/output/output.ac.frcmod --output_path_inpcrd data/output/output.ac.inpcrd --output_path_lib data/output/output.ac.lib --output_path_prmtop data/output/output.ac.prmtop

JSON file config
~~~~~~~~~~~~~~~~

ac.json:

.. parsed-literal::

    {
      "properties": {
        "basename": "BBB",
        "charge": 0
      }
    }

Command:

.. parsed-literal::

    acpype_params_ac --config data/conf/ac.json --input_path data/input/acpype.params.mol2 --output_path_frcmod data/output/output.ac.frcmod --output_path_inpcrd data/output/output.ac.inpcrd --output_path_lib data/output/output.ac.lib --output_path_prmtop data/output/output.ac.prmtop

Acpype params CNS
-----------------

Wrapper for the Acpype module. Generation of topologies for CNS/XPLOR.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    acpype_params_cns -h

.. parsed-literal::

    usage: acpype_params_cns [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_path INPUT_PATH --output_path_par OUTPUT_PATH_PAR --output_path_inp OUTPUT_PATH_INP --output_path_top OUTPUT_PATH_TOP
    
    Wrapper for the Acpype module. Generation of topologies for CNS/XPLOR.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_path INPUT_PATH
                            Path to the input file. Accepted formats: pdb, mdl, mol2.
      --output_path_par OUTPUT_PATH_PAR
                            Path to the PAR output file. Accepted format: par.
      --output_path_inp OUTPUT_PATH_INP
                            Path to the INP output file. Accepted format: inp.
      --output_path_top OUTPUT_PATH_TOP
                            Path to the TOP output file. Accepted format: top.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_path** (*str*): Path to the input file. Accepted formats:
   pdb, mdl, mol2.
-  **output_path_par** (*str*): Path to the PAR output file. Accepted
   format: par.
-  **output_path_inp** (*str*): Path to the INP output file. Accepted
   format: inp.
-  **output_path_top** (*str*): Path to the TOP output file. Accepted
   format: top.

Config
~~~~~~

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **basename** (*str*) - (“BBB”) A basename for the project (folder and
   output files).
-  **charge** (*int*) - (0) Net molecular charge, for gas default is 0.
-  **acpype_path** (*str*) - (“acpype”) Path to the acpype executable
   binary.

YAML file config
~~~~~~~~~~~~~~~~

cns.yml:

.. parsed-literal::

    properties:
      basename: "BBB"
      charge: 0

Command:

.. parsed-literal::

    acpype_params_cns --config data/conf/cns.yml --input_path data/input/acpype.params.mol2 --output_path_par data/output/output.cns.par --output_path_inp data/output/output.cns.inp --output_path_top data/output/output.cns.top

JSON file config
~~~~~~~~~~~~~~~~

cns.json:

.. parsed-literal::

    {
      "properties": {
        "basename": "BBB",
        "charge": 0
      }
    }

Command:

.. parsed-literal::

    acpype_params_cns --config data/conf/cns.json --input_path data/input/acpype.params.mol2 --output_path_par data/output/output.cns.par --output_path_inp data/output/output.cns.inp --output_path_top data/output/output.cns.top 

Acpype params GMX
-----------------

Wrapper for the Acpype module. Generation of topologies for GROMACS.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    acpype_params_gmx -h

.. parsed-literal::

    usage: acpype_params_gmx [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_path INPUT_PATH --output_path_gro OUTPUT_PATH_GRO --output_path_itp OUTPUT_PATH_ITP --output_path_top OUTPUT_PATH_TOP
    
    Wrapper for the Acpype module. Generation of topologies for GROMACS.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_path INPUT_PATH
                            Path to the input file. Accepted formats: pdb, mdl, mol2.
      --output_path_gro OUTPUT_PATH_GRO
                            Path to the GRO output file. Accepted format: gro.
      --output_path_itp OUTPUT_PATH_ITP
                            Path to the ITP output file. Accepted format: itp.
      --output_path_top OUTPUT_PATH_TOP
                            Path to the TOP output file. Accepted format: top.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_path** (*str*): Path to the input file. Accepted formats:
   pdb, mdl, mol2.
-  **output_path_gro** (*str*): Path to the GRO output file. Accepted
   format: gro.
-  **output_path_itp** (*str*): Path to the ITP output file. Accepted
   format: itp.
-  **output_path_top** (*str*): Path to the TOP output file. Accepted
   format: top.

Config
~~~~~~

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **basename** (*str*) - (“BBB”) A basename for the project (folder and
   output files).
-  **charge** (*int*) - (0) Net molecular charge, for gas default is 0.
-  **acpype_path** (*str*) - (“acpype”) Path to the acpype executable
   binary.

YAML file config
~~~~~~~~~~~~~~~~

gmx.yml:

.. parsed-literal::

    properties:
      basename: "BBB"
      charge: 0

Command:

.. parsed-literal::

    acpype_params_gmx --config data/conf/gmx.yml --input_path data/input/acpype.params.mol2 --output_path_gro data/output/output.gmx.gro --output_path_itp data/output/output.gmx.itp --output_path_top data/output/output.gmx.top

JSON file config
~~~~~~~~~~~~~~~~

gmx.json:

.. parsed-literal::

    {
      "properties": {
        "basename": "BBB",
        "charge": 0
      }
    }

Command:

.. parsed-literal::

    acpype_params_gmx --config data/conf/gmx.json --input_path data/input/acpype.params.mol2 --output_path_gro data/output/output.gmx.gro --output_path_itp data/output/output.gmx.itp --output_path_top data/output/output.gmx.top

Acpype params GMX OPLS
----------------------

Wrapper for the Acpype module. Generation of topologies for OPLS/AA.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    acpype_params_gmx_opls -h

.. parsed-literal::

    usage: acpype_params_gmx_opls [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_path INPUT_PATH --output_path_itp OUTPUT_PATH_ITP --output_path_top OUTPUT_PATH_TOP
    
    Wrapper for the Acpype module. Generation of topologies for OPLS/AA.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_path INPUT_PATH
                            Path to the input file. Accepted formats: pdb, mdl, mol2.
      --output_path_itp OUTPUT_PATH_ITP
                            Path to the ITP output file. Accepted format: itp.
      --output_path_top OUTPUT_PATH_TOP
                            Path to the TOP output file. Accepted format: top.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_path** (*str*): Path to the input file. Accepted formats:
   pdb, mdl, mol2.
-  **output_path_itp** (*str*): Path to the ITP output file. Accepted
   format: itp.
-  **output_path_top** (*str*): Path to the TOP output file. Accepted
   format: top.

Config
~~~~~~

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **basename** (*str*) - (“BBB”) A basename for the project (folder and
   output files).
-  **charge** (*int*) - (0) Net molecular charge, for gas default is 0.
-  **acpype_path** (*str*) - (“acpype”) Path to the acpype executable
   binary.

YAML file config
~~~~~~~~~~~~~~~~

gmx.yml:

.. parsed-literal::

    properties:
      basename: "BBB"
      charge: 0

Command:

.. parsed-literal::

    acpype_params_gmx_opls --config data/conf/gmx.yml --input_path data/input/acpype.params.mol2 --output_path_itp data/output/output.gmx.opls.itp --output_path_top data/output/output.gmx.opls.top

JSON file config
~~~~~~~~~~~~~~~~

gmx.json:

.. parsed-literal::

    {
      "properties": {
        "basename": "BBB",
        "charge": 0
      }
    }

Command:

.. parsed-literal::

    acpype_params_gmx_opls --config data/conf/gmx.json --input_path data/input/acpype.params.mol2 --output_path_itp data/output/output.gmx.itp --output_path_top data/output/output.gmx.top

Babel add hydrogens
-------------------

Wrapper of the Open Babel module. Adds hydrogens to a given structure or
trajectory.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    babel_add_hydrogens -h

.. parsed-literal::

    usage: babel_add_hydrogens [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_path INPUT_PATH --output_path OUTPUT_PATH
    
    Wrapper for the Open Babel module. Adds hydrogens to a given structure or trajectory.
    
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

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_path** (*str*): Path to the input file. Accepted formats:
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
-  **output_path** (*str*): Path to the output file. Accepted formats:
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

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **input_format** (*str*) - (None) Format of input file. If not
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
-  **output_format** (*str*) - (None) Format of output file. If not
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
-  **obabel_path** (*str*) - (“obabel”) Path to the obabel executable
   binary.

YAML file config
~~~~~~~~~~~~~~~~

add_hydrogens.yml:

.. parsed-literal::

    properties:
      input_format: pdb
      output_format: pdb
      coordinates: 3
      ph: 7.4

Command:

.. parsed-literal::

    babel_add_hydrogens --config data/conf/add_hydrogens.yml --input_path data/input/babel.no.H.pdb --output_path data/output/output.add.H.pdb

JSON file config
~~~~~~~~~~~~~~~~

add_hydrogens.json:

.. parsed-literal::

    {
      "properties": {
        "input_format": "pdb",
        "output_format": "pdb",
        "coordinates": 3,
        "ph": 7.4
      }
    }

Command:

.. parsed-literal::

    babel_add_hydrogens --config data/conf/add_hydrogens.json --input_path data/input/babel.no.H.pdb --output_path data/output/output.add.H.pdb

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

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_path** (*str*): Path to the input file. Accepted formats:
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
-  **output_path** (*str*): Path to the output file. Accepted formats:
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

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **input_format** (*str*) - (None) Format of input file. If not
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
-  **output_format** (*str*) - (None) Format of output file. If not
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
-  **obabel_path** (*str*) - (“obabel”) Path to the obabel executable
   binary.

YAML file config
~~~~~~~~~~~~~~~~

convert.yml:

.. parsed-literal::

    properties:
      input_format: smi
      output_format: pdb
      coordinates: 2
      ph: 7.4

Command:

.. parsed-literal::

    babel_convert --config data/conf/convert.yml --input_path data/input/babel.smi --output_path data/output/output.convert.pdb

JSON file config
~~~~~~~~~~~~~~~~

convert.json:

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

    babel_convert --config data/conf/convert.json --input_path data/input/babel.smi --output_path data/output/output.convert.pdb

Babel minimize
--------------

Wrapper of the Open Babel module. Structure minimization.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    babel_minimize -h

.. parsed-literal::

    usage: babel_minimize [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_path INPUT_PATH --output_path OUTPUT_PATH
    
    Wrapper for the Open Babel module. Structure minimization.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_path INPUT_PATH
                            Path to the input file. Accepted formats: pdb, mol2.
      --output_path OUTPUT_PATH
                            Path to the output file. Accepted formats: pdb, mol2.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_path** (*str*): Path to the input file. Accepted formats:
   pdb, mol2.
-  **output_path** (*str*): Path to the output file. Accepted formats:
   pdb, mol2.

Config
~~~~~~

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **criteria** (*float*) - (1e-6) Convergence criteria
-  **method** (*str*) - (“cg”) Method. Values: cg (conjugate gradients
   algorithm), sd (steepest descent algorithm).
-  **force_field** (*str*) - (None) Force field. Values: GAFF (General
   Amber Force Field), Ghemical (Ghemical force field), MMFF94 (MMFF94
   force field), MMFF94s (MMFF94s force field), UFF (Universal Force
   Field).
-  **hydrogens** (*bool*) - (False) Add hydrogen atoms.
-  **steps** (*int*) - (2500) Maximum number of steps.
-  **cutoff** (*bool*) - (False) Use cut-off.
-  **rvdw** (*float*) - (6.0) VDW cut-off distance.
-  **rele** (*float*) - (10.0) Electrostatic cut-off distance.
-  **frequency** (*int*) - (10) Frequency to update the non-bonded
   pairs.
-  **obminimize_path** (*str*) - (“obminimize”) Path to the obminimize
   executable binary.

YAML file config
~~~~~~~~~~~~~~~~

minimize.yml:

.. parsed-literal::

    properties:
      criteria: 1e-6
      method: cg
      force_field: GAFF
      hydrogens: True
      steps: 2500
      cutoff: True
      rvdw: 6.0
      rele: 10.0
      frequency: 10

Command:

.. parsed-literal::

    babel_minimize --config data/conf/minimize.yml --input_path data/input/babel.minimize.pdb --output_path data/output/output.minimize.pdb

JSON file config
~~~~~~~~~~~~~~~~

minimize.json:

.. parsed-literal::

    {
      "properties": {
        "criteria": 1e-6,
        "method": "cg",
        "force_field": "GAFF",
        "hydrogens": true,
        "steps": 2500,
        "cutoff": true,
        "rvdw": 6.0,
        "rele": 10.0,
        "frequency": 10
      }
    }

Command:

.. parsed-literal::

    babel_minimize --config data/conf/minimize.json --input_path data/input/babel.minimize.pdb --output_path data/output/output.minimize.pdb

Babel remove hydrogens
----------------------

Wrapper of the Open Babel module. Removes hydrogens to a given structure
or trajectory.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    babel_remove_hydrogens -h

.. parsed-literal::

    usage: babel_remove_hydrogens [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_path INPUT_PATH --output_path OUTPUT_PATH
    
    Wrapper for the Open Babel module. Removes hydrogens to a given structure or trajectory.
    
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

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_path** (*str*): Path to the input file. Accepted formats:
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
-  **output_path** (*str*): Path to the output file. Accepted formats:
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

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **input_format** (*str*) - (None) Format of input file. If not
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
-  **output_format** (*str*) - (None) Format of output file. If not
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
-  **obabel_path** (*str*) - (“obabel”) Path to the obabel executable
   binary.

YAML file config
~~~~~~~~~~~~~~~~

remove_hydrogens.yml:

.. parsed-literal::

    properties:
      input_format: pdb
      output_format: pdb
      coordinates: 3
      ph: 7.4

Command:

.. parsed-literal::

    babel_remove_hydrogens --config data/conf/remove_hydrogens.yml --input_path data/input/babel.H.pdb --output_path data/output/output.remove.H.pdb

JSON file config
~~~~~~~~~~~~~~~~

remove_hydrogens.json:

.. parsed-literal::

    {
      "properties": {
        "input_format": "pdb",
        "output_format": "pdb",
        "coordinates": 3,
        "ph": 7.4
      }
    }

Command:

.. parsed-literal::

    babel_remove_hydrogens --config data/conf/remove_hydrogens.json --input_path data/input/babel.H.pdb --output_path data/output/output.remove.H.pdb

Reduce add hydrogens
--------------------

Wrapper of the Ambertools reduce module. Adds hydrogens to a given
structure.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    reduce_add_hydrogens -h

.. parsed-literal::

    usage: reduce_add_hydrogens [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_path INPUT_PATH --output_path OUTPUT_PATH
    
    Wrapper of the Ambertools reduce module. Adds hydrogens to a given structure.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_path INPUT_PATH
                            Path to the input file. Accepted formats: pdb, mol2.
      --output_path OUTPUT_PATH
                            Path to the output file. Accepted formats: pdb, mol2.

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_path** (*str*): Path to the input file. Accepted format: pdb.
-  **output_path** (*str*): Path to the output file. Accepted format:
   pdb.

Config
~~~~~~

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **flip** (*Boolean*) - (False) add H and rotate and flip NQH groups
-  **noflip** (*Boolean*) - (False) add H and rotate groups with no NQH
   flips
-  **nuclear** (*Boolean*) - (False) use nuclear X-H distances rather
   than default electron cloud distances
-  **nooh** (*Boolean*) - (False) remove hydrogens on OH and SH groups
-  **oh** (*Boolean*) - (True) add hydrogens on OH and SH groups
   (default)
-  **his** (*Boolean*) - (False) create NH hydrogens on HIS rings
   (usually used with -HIS)
-  **noheth** (*Boolean*) - (False) do not attempt to add NH proton on
   Het groups
-  **rotnh3** (*Boolean*) - (True) allow lysine NH3 to rotate (default)
-  **norotnh3** (*Boolean*) - (False) do not allow lysine NH3 to rotate
-  **rotexist** (*Boolean*) - (False) allow existing rotatable groups
   (OH, SH, Met-CH3) to rotate
-  **rotexoh** (*Boolean*) - (False) allow existing OH & SH groups to
   rotate
-  **allalt** (*Boolean*) - (True) process adjustments for all
   conformations (default)
-  **onlya** (*Boolean*) - (False) only adjust ‘A’ conformations
-  **charges** (*Boolean*) - (False) output charge state for appropriate
   hydrogen records
-  **dorotmet** (*Boolean*) - (False) allow methionine methyl groups to
   rotate (not recommended)
-  **noadjust** (*Boolean*) - (False) do not process any rot or flip
   adjustments
-  **build** (*Boolean*) - (False) add H, including His sc NH, then
   rotate and flip groups (except for pre-existing methionine methyl
   hydrogens)
-  **reduce_path** (*str*) - (“reduce”) Path to the reduce executable
   binary.

YAML file config
~~~~~~~~~~~~~~~~

reduce_add_hydrogens.yml:

.. parsed-literal::

    properties:
      nooh: True

Command:

.. parsed-literal::

    reduce_add_hydrogens --config data/conf/reduce_add_hydrogens.yml --input_path data/input/reduce.no.H.pdb --output_path data/output/output.reduce.H.pdb

JSON file config
~~~~~~~~~~~~~~~~

remove_hydrogens.json:

.. parsed-literal::

    {
      "properties": {
        "nooh": true
      }
    }

Command:

.. parsed-literal::

    reduce_add_hydrogens --config data/conf/reduce_add_hydrogens.json --input_path data/input/reduce.no.H.pdb --output_path data/output/output.reduce.H.pdb

Reduce remove hydrogens
-----------------------

Wrapper of the Ambertools reduce module. Removes hydrogens from a given
structure.

Get help
~~~~~~~~

Command:

.. parsed-literal::

    reduce_remove_hydrogens -h

.. parsed-literal::

    usage: reduce_remove_hydrogens [-h] [--config CONFIG] [--system SYSTEM] [--step STEP] --input_path INPUT_PATH --output_path OUTPUT_PATH
    
    Wrapper of the Ambertools reduce module. Removes hydrogens from a given structure.
    
    optional arguments:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
      --system SYSTEM       Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
      --step STEP           Check 'https://biobb-common.readthedocs.io/en/latest/system_step.html' for help
    
    required arguments:
      --input_path INPUT_PATH
                            Path to the input file. Accepted formats: pdb, mol2
      --output_path OUTPUT_PATH
                            Path to the output file. Accepted formats: pdb, mol2

I / O Arguments
~~~~~~~~~~~~~~~

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

-  **input_path** (*str*): Path to the input file. Accepted format: pdb.
-  **output_path** (*str*): Path to the output file. Accepted format:
   pdb.

Config
~~~~~~

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

-  **reduce_path** (*str*) - (“reduce”) Path to the reduce executable
   binary.

YAML file config
~~~~~~~~~~~~~~~~

reduce_remove_hydrogens.yml:

.. parsed-literal::

    properties:
      reduce_path: "reduce"

Command:

.. parsed-literal::

    reduce_remove_hydrogens --config data/conf/reduce_remove_hydrogens.yml --input_path data/input/reduce.H.pdb --output_path data/output/output.reduce.pdb

JSON file config
~~~~~~~~~~~~~~~~

reduce_remove_hydrogens.json:

.. parsed-literal::

    {
      "properties": {
        "reduce_path": "reduce"
      }
    }

Command:

.. parsed-literal::

    reduce_remove_hydrogens --config data/conf/reduce_remove_hydrogens.json --input_path data/input/reduce.H.pdb --output_path data/output/output.reduce.pdb

