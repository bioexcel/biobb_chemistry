# BioBB Chemistry Command Line Help

Generic usage:


```python
biobb_command [-h] --config CONFIG --input_file(s) <input_file(s)> --output_file <output_file>
```

-----------------

## Acpype params AC

Small molecule parameterization for AMBER MD package.

### Get help

Command:


```python
acpype_params_ac -h
```


```python
usage: acpype_params_ac [-h] [--config CONFIG] --input_path INPUT_PATH --output_path_frcmod OUTPUT_PATH_FRCMOD --output_path_inpcrd OUTPUT_PATH_INPCRD --output_path_lib OUTPUT_PATH_LIB --output_path_prmtop OUTPUT_PATH_PRMTOP

Small molecule parameterization for AMBER MD package.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Configuration file

required arguments:
  --input_path INPUT_PATH
                        Path to the input file. Accepted formats: pdb, mdl, mol2.
  --output_path_frcmod OUTPUT_PATH_FRCMOD
                        Path to the FRCMOD output file. Accepted formats: frcmod.
  --output_path_inpcrd OUTPUT_PATH_INPCRD
                        Path to the INPCRD output file. Accepted formats: inpcrd.
  --output_path_lib OUTPUT_PATH_LIB
                        Path to the LIB output file. Accepted formats: lib.
  --output_path_prmtop OUTPUT_PATH_PRMTOP
                        Path to the PRMTOP output file. Accepted formats: prmtop.
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_path** (*str*): Path to the input file. File type: input. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/acpype/acpype.params.mol2). Accepted formats: pdb, mdl, mol2.
* **output_path_frcmod** (*str*): Path to the FRCMOD output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.ac.frcmod). Accepted formats: frcmod.
* **output_path_inpcrd** (*str*): Path to the INPCRD output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.ac.inpcrd). Accepted formats: inpcrd.
* **output_path_lib** (*str*): Path to the LIB output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.ac.lib). Accepted formats: lib.
* **output_path_prmtop** (*str*): Path to the PRMTOP output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.ac.prmtop). Accepted formats: prmtop.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **basename** (*str*) - ("BBB") A basename for the project (folder and output files).
* **charge** (*int*) - (0) Net molecular charge, for gas default is 0.
* **acpype_path** (*str*) - ("acpype") Path to the acpype executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('mmbirb/acpype:latest') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML

#### Common file config


```python
properties:
  basename: "BBB"
  charge: 0
```

#### Docker file config


```python
properties:
  basename: "BBB"
  charge: 0
  container_path: docker
  container_image: mmbirb/acpype:latest
  container_volume_path: /tmp
  container_working_dir: /tmp
  container_shell_path: /bin/sh
```

#### Singularity file config


```python
properties:
  basename: "BBB"
  charge: 0
  container_path: singularity
  container_image: shub://bioexcel/acpype_container
  container_volume_path: /tmp
  container_working_dir: /tmp
  container_shell_path: /bin/sh
```

#### Command line


```python
acpype_params_ac --config data/conf/ac.yml --input_path data/input/acpype.params.mol2 --output_path_frcmod data/output/output.ac.frcmod --output_path_inpcrd data/output/output.ac.inpcrd --output_path_lib data/output/output.ac.lib --output_path_prmtop data/output/output.ac.prmtop
```

### JSON

#### Common file config


```python
{
  "properties": {
    "basename": "BBB",
    "charge": 0
  }
}
```

#### Docker file config


```python
{
  "properties": {
    "basename": "BBB",
    "charge": 0,
    "container_path": "docker",
    "container_image": "mmbirb/acpype:latest",
    "container_volume_path": "/tmp",
    "container_working_dir": "/tmp",
    "container_shell_path": "/bin/sh"
  }
}
```

#### Singularity file config


```python
{
  "properties": {
    "basename": "BBB",
    "charge": 0,
    "container_path": "singularity",
    "container_image": "shub://bioexcel/acpype_container",
    "container_volume_path": "/tmp",
    "container_working_dir": "/tmp",
    "container_shell_path": "/bin/sh"
  }
}
```

#### Command line


```python
acpype_params_ac --config data/conf/ac.json --input_path data/input/acpype.params.mol2 --output_path_frcmod data/output/output.ac.frcmod --output_path_inpcrd data/output/output.ac.inpcrd --output_path_lib data/output/output.ac.lib --output_path_prmtop data/output/output.ac.prmtop
```

## Acpype params CNS

Small molecule parameterization for CNS/XPLOR MD package.

### Get help

Command:


```python
acpype_params_cns -h
```


```python
usage: acpype_params_cns [-h] [--config CONFIG] --input_path INPUT_PATH --output_path_par OUTPUT_PATH_PAR --output_path_inp OUTPUT_PATH_INP --output_path_top OUTPUT_PATH_TOP

Small molecule parameterization for CNS/XPLOR MD package.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Configuration file

required arguments:
  --input_path INPUT_PATH
                        Path to the input file. Accepted formats: pdb, mdl, mol2.
  --output_path_par OUTPUT_PATH_PAR
                        Path to the PAR output file. Accepted formats: par.
  --output_path_inp OUTPUT_PATH_INP
                        Path to the INP output file. Accepted formats: inp.
  --output_path_top OUTPUT_PATH_TOP
                        Path to the TOP output file. Accepted formats: top.
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_path** (*str*): Path to the input file. File type: input. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/acpype/acpype.params.mol2). Accepted formats: pdb, mdl, mol2.
* **output_path_par** (*str*): Path to the PAR output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.cns.par). Accepted formats: par.
* **output_path_inp** (*str*): Path to the INP output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.cns.inp). Accepted formats: inp.
* **output_path_top** (*str*): Path to the TOP output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.cns.top). Accepted formats: top.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **basename** (*str*) - ("BBB") A basename for the project (folder and output files).
* **charge** (*int*) - (0) Net molecular charge, for gas default is 0.
* **acpype_path** (*str*) - ("acpype") Path to the acpype executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('mmbirb/acpype:latest') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML

#### Common file config


```python
properties:
  basename: "BBB"
  charge: 0
```

#### Docker file config


```python
properties:
  basename: "BBB"
  charge: 0
  container_path: docker
  container_image: mmbirb/acpype:latest
  container_volume_path: /tmp
  container_working_dir: /tmp
  container_shell_path: /bin/sh
```

#### Singularity file config


```python
properties:
  basename: "BBB"
  charge: 0
  container_path: singularity
  container_image: shub://bioexcel/acpype_container
  container_volume_path: /tmp
  container_working_dir: /tmp
  container_shell_path: /bin/sh
```

#### Command line


```python
acpype_params_cns --config data/conf/cns.yml --input_path data/input/acpype.params.mol2 --output_path_par data/output/output.cns.par --output_path_inp data/output/output.cns.inp --output_path_top data/output/output.cns.top
```

### JSON

#### Common file config


```python
{
  "properties": {
    "basename": "BBB",
    "charge": 0
  }
}
```

#### Docker file config


```python
{
  "properties": {
    "basename": "BBB",
    "charge": 0,
    "container_path": "docker",
    "container_image": "mmbirb/acpype:latest",
    "container_volume_path": "/tmp",
    "container_working_dir": "/tmp",
    "container_shell_path": "/bin/sh"
  }
}
```

#### Singularity file config


```python
{
  "properties": {
    "basename": "BBB",
    "charge": 0,
    "container_path": "singularity",
    "container_image": "shub://bioexcel/acpype_container",
    "container_volume_path": "/tmp",
    "container_working_dir": "/tmp",
    "container_shell_path": "/bin/sh"
  }
}
```

#### Command line


```python
acpype_params_cns --config data/conf/cns.json --input_path data/input/acpype.params.mol2 --output_path_par data/output/output.cns.par --output_path_inp data/output/output.cns.inp --output_path_top data/output/output.cns.top 
```

## Acpype params GMX

Small molecule parameterization for GROMACS MD package.

### Get help

Command:


```python
acpype_params_gmx -h
```


```python
usage: acpype_params_gmx [-h] [--config CONFIG] --input_path INPUT_PATH --output_path_gro OUTPUT_PATH_GRO --output_path_itp OUTPUT_PATH_ITP --output_path_top OUTPUT_PATH_TOP

Small molecule parameterization for GROMACS MD package.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Configuration file

required arguments:
  --input_path INPUT_PATH
                        Path to the input file. Accepted formats: pdb, mdl, mol2.
  --output_path_gro OUTPUT_PATH_GRO
                        Path to the GRO output file. Accepted formats: gro.
  --output_path_itp OUTPUT_PATH_ITP
                        Path to the ITP output file. Accepted formats: itp.
  --output_path_top OUTPUT_PATH_TOP
                        Path to the TOP output file. Accepted formats: top.
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_path** (*str*): Path to the input file. File type: input. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/acpype/acpype.params.mol2). Accepted formats: pdb, mdl, mol2.
* **output_path_gro** (*str*): Path to the GRO output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.gmx.gro). Accepted formats: gro.
* **output_path_itp** (*str*): Path to the ITP output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.gmx.itp). Accepted formats: itp.
* **output_path_top** (*str*): Path to the TOP output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.gmx.top). Accepted formats: top.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **basename** (*str*) - ("BBB") A basename for the project (folder and output files).
* **charge** (*int*) - (0) Net molecular charge, for gas default is 0.
* **acpype_path** (*str*) - ("acpype") Path to the acpype executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('mmbirb/acpype:latest') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML

#### Common file config


```python
properties:
  basename: "BBB"
  charge: 0
```

#### Docker file config


```python
properties:
  basename: "BBB"
  charge: 0
  container_path: docker
  container_image: mmbirb/acpype:latest
  container_volume_path: /tmp
  container_working_dir: /tmp
  container_shell_path: /bin/sh
```

#### Singularity file config


```python
properties:
  basename: "BBB"
  charge: 0
  container_path: singularity
  container_image: shub://bioexcel/acpype_container
  container_volume_path: /tmp
  container_working_dir: /tmp
  container_shell_path: /bin/sh
```

#### Command line


```python
acpype_params_gmx --config data/conf/gmx.yml --input_path data/input/acpype.params.mol2 --output_path_gro data/output/output.gmx.gro --output_path_itp data/output/output.gmx.itp --output_path_top data/output/output.gmx.top
```

### JSON

#### Common file config


```python
{
  "properties": {
    "basename": "BBB",
    "charge": 0
  }
}
```

#### Docker file config


```python
{
  "properties": {
    "basename": "BBB",
    "charge": 0,
    "container_path": "docker",
    "container_image": "mmbirb/acpype:latest",
    "container_volume_path": "/tmp",
    "container_working_dir": "/tmp",
    "container_shell_path": "/bin/sh"
  }
}
```

#### Singularity file config


```python
{
  "properties": {
    "basename": "BBB",
    "charge": 0,
    "container_path": "singularity",
    "container_image": "shub://bioexcel/acpype_container",
    "container_volume_path": "/tmp",
    "container_working_dir": "/tmp",
    "container_shell_path": "/bin/sh"
  }
}
```

#### Command line


```python
acpype_params_gmx --config data/conf/gmx.json --input_path data/input/acpype.params.mol2 --output_path_gro data/output/output.gmx.gro --output_path_itp data/output/output.gmx.itp --output_path_top data/output/output.gmx.top
```

## Acpype params GMX OPLS

Small molecule parameterization for OPLS/AA MD package.

### Get help

Command:


```python
acpype_params_gmx_opls -h
```


```python
usage: acpype_params_gmx_opls [-h] [--config CONFIG] --input_path INPUT_PATH --output_path_itp OUTPUT_PATH_ITP --output_path_top OUTPUT_PATH_TOP

Small molecule parameterization for OPLS/AA MD package.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Configuration file

required arguments:
  --input_path INPUT_PATH
                        Path to the input file. Accepted formats: pdb, mdl, mol2.
  --output_path_itp OUTPUT_PATH_ITP
                        Path to the ITP output file. Accepted formats: itp.
  --output_path_top OUTPUT_PATH_TOP
                        Path to the TOP output file. Accepted formats: top.
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_path** (*str*): Path to the input file. File type: input. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/acpype/acpype.params.mol2). Accepted formats: pdb, mdl, mol2.
* **output_path_itp** (*str*): Path to the ITP output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.gmx.opls.itp). Accepted formats: itp.
* **output_path_top** (*str*): Path to the TOP output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.gmx.opls.top). Accepted formats: top.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **basename** (*str*) - ("BBB") A basename for the project (folder and output files).
* **charge** (*int*) - (0) Net molecular charge, for gas default is 0.
* **acpype_path** (*str*) - ("acpype") Path to the acpype executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('mmbirb/acpype:latest') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML

### YAML file config

#### Common file config


```python
properties:
  basename: "BBB"
  charge: 0
```

#### Docker file config


```python
properties:
  basename: "BBB"
  charge: 0
  container_path: docker
  container_image: mmbirb/acpype:latest
  container_volume_path: /tmp
  container_working_dir: /tmp
  container_shell_path: /bin/sh
```

#### Singularity file config


```python
properties:
  basename: "BBB"
  charge: 0
  container_path: singularity
  container_image: shub://bioexcel/acpype_container
  container_volume_path: /tmp
  container_working_dir: /tmp
  container_shell_path: /bin/sh
```

#### Command line


```python
acpype_params_gmx_opls --config data/conf/gmx.yml --input_path data/input/acpype.params.mol2 --output_path_itp data/output/output.gmx.opls.itp --output_path_top data/output/output.gmx.opls.top
```

### JSON

#### Common  file config


```python
{
  "properties": {
    "basename": "BBB",
    "charge": 0
  }
}
```

#### Docker  file config


```python
{
  "properties": {
    "basename": "BBB",
    "charge": 0,
    "container_path": "docker",
    "container_image": "mmbirb/acpype:latest",
    "container_volume_path": "/tmp",
    "container_working_dir": "/tmp",
    "container_shell_path": "/bin/sh"
  }
}
```

#### Singularity  file config


```python
{
  "properties": {
    "basename": "BBB",
    "charge": 0,
    "container_path": "singularity",
    "container_image": "shub://bioexcel/acpype_container",
    "container_volume_path": "/tmp",
    "container_working_dir": "/tmp",
    "container_shell_path": "/bin/sh"
  }
}
```

#### Command line


```python
acpype_params_gmx_opls --config data/conf/gmx.json --input_path data/input/acpype.params.mol2 --output_path_itp data/output/output.gmx.itp --output_path_top data/output/output.gmx.top
```

## Babel add hydrogens

Adds hydrogen atoms to small molecules.

### Get help

Command:


```python
babel_add_hydrogens -h
```


```python
usage: babel_add_hydrogens [-h] [--config CONFIG] --input_path INPUT_PATH --output_path OUTPUT_PATH

Adds hydrogen atoms to small molecules.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Configuration file

required arguments:
  --input_path INPUT_PATH
                        Path to the input file. Accepted formats: abinit, acesout, acr, adfout, alc, aoforce, arc, axsf, bgf, box, bs, c09out, c3d2, caccrt, can, car, castep, ccc, cdjson, cdx, cdxml, cif, ck, cml, cmlr, CONFIG, CONTCAR, CONTFF, crk2d, crk3d, ct, cub, cube, dallog, dalmol, dat, dmol, dx, ent, exyz, fa, fasta, fch, fchk, fck, feat, fhiaims, fract, fs, fsa, g03, g09, g92, g94, g98, gal, gam, gamess, gamin, gamout, got, gpr, gro, gukin, gukout, gzmat, hin, HISTORY, inchi, inp, ins, jin, jout, log, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mol, mol2, mold, molden, molf, moo, mop, mopcrt, mopin, mopout, mpc, mpo, mpqc, mrv, msi, nwo, orca, out, outmol, output, pc, pcjson, pcm, pdb, pdbqt, png, pos, POSCAR, POSFF, pqr, pqs, prep, pwscf, qcout, res, rsmi, rxn, sd, sdf, siesta, smi, smiles, smy, sy2, t41, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xml, xsf, xtc, xyz, yob.
  --output_path OUTPUT_PATH
                        Path to the output file. Accepted formats: acesin, adf, alc, ascii, bgf, box, bs, c3d1, c3d2, cac, caccrt, cache, cacint, can, cdjson, cdxml, cht, cif, ck, cml, cmlr, com, confabreport, CONFIG, CONTCAR, CONTFF, copy, crk2d, crk3d, csr, cssr, ct, cub, cube, dalmol, dmol, dx, ent, exyz, fa, fasta, feat, fh, fhiaims, fix, fps, fpt, fract, fs, fsa, gamin, gau, gjc, gjf, gpr, gr96, gro, gukin, gukout, gzmat, hin, inchi, inchikey, inp, jin, k, lmpdat, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mna, mol, mol2, mold, molden, molf, molreport, mop, mopcrt, mopin, mp, mpc, mpd, mpqcin, mrv, msms, nul, nw, orcainp, outmol, paint, pcjson, pcm, pdb, pdbqt, png, pointcloud, POSCAR, POSFF, pov, pqr, pqs, qcin, report, rsmi, rxn, sd, sdf, smi, smiles, stl, svg, sy2, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xed, xyz, yob, zin.
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_path** (*str*): Path to the input file. File type: input. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/babel/babel.no.H.pdb). Accepted formats: abinit, acesout, acr, adfout, alc, aoforce, arc, axsf, bgf, box, bs, c09out, c3d2, caccrt, can, car, castep, ccc, cdjson, cdx, cdxml, cif, ck, cml, cmlr, CONFIG, CONTCAR, CONTFF, crk2d, crk3d, ct, cub, cube, dallog, dalmol, dat, dmol, dx, ent, exyz, fa, fasta, fch, fchk, fck, feat, fhiaims, fract, fs, fsa, g03, g09, g92, g94, g98, gal, gam, gamess, gamin, gamout, got, gpr, gro, gukin, gukout, gzmat, hin, HISTORY, inchi, inp, ins, jin, jout, log, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mol, mol2, mold, molden, molf, moo, mop, mopcrt, mopin, mopout, mpc, mpo, mpqc, mrv, msi, nwo, orca, out, outmol, output, pc, pcjson, pcm, pdb, pdbqt, png, pos, POSCAR, POSFF, pqr, pqs, prep, pwscf, qcout, res, rsmi, rxn, sd, sdf, siesta, smi, smiles, smy, sy2, t41, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xml, xsf, xtc, xyz, yob.
* **output_path** (*str*): Path to the output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/babel/ref_babel.hydrogens.pdb). Accepted formats: acesin, adf, alc, ascii, bgf, box, bs, c3d1, c3d2, cac, caccrt, cache, cacint, can, cdjson, cdxml, cht, cif, ck, cml, cmlr, com, confabreport, CONFIG, CONTCAR, CONTFF, copy, crk2d, crk3d, csr, cssr, ct, cub, cube, dalmol, dmol, dx, ent, exyz, fa, fasta, feat, fh, fhiaims, fix, fps, fpt, fract, fs, fsa, gamin, gau, gjc, gjf, gpr, gr96, gro, gukin, gukout, gzmat, hin, inchi, inchikey, inp, jin, k, lmpdat, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mna, mol, mol2, mold, molden, molf, molreport, mop, mopcrt, mopin, mp, mpc, mpd, mpqcin, mrv, msms, nul, nw, orcainp, outmol, paint, pcjson, pcm, pdb, pdbqt, png, pointcloud, POSCAR, POSFF, pov, pqr, pqs, qcin, report, rsmi, rxn, sd, sdf, smi, smiles, stl, svg, sy2, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xed, xyz, yob, zin.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **input_format** (*str*) - (None) Format of input file. If not provided, file extension will be taken. Values: abinit, acesout, acr, adfout, alc, aoforce, arc, axsf, bgf, box, bs, c09out, c3d2, caccrt, can, car, castep, ccc, cdjson, cdx, cdxml, cif, ck, cml, cmlr, CONFIG, CONTCAR, CONTFF, crk2d, crk3d, ct, cub, cube, dallog, dalmol, dat, dmol, dx, ent, exyz, fa, fasta, fch, fchk, fck, feat, fhiaims, fract, fs, fsa, g03, g09, g92, g94, g98, gal, gam, gamess, gamin, gamout, got, gpr, gro, gukin, gukout, gzmat, hin, HISTORY, inchi, inp, ins, jin, jout, log, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mol, mol2, mold, molden, molf, moo, mop, mopcrt, mopin, mopout, mpc, mpo, mpqc, mrv, msi, nwo, orca, out, outmol, output, pc, pcjson, pcm, pdb, pdbqt, png, pos, POSCAR, POSFF, pqr, pqs, prep, pwscf, qcout, res, rsmi, rxn, sd, sdf, siesta, smi, smiles, smy, sy2, t41, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xml, xsf, xtc, xyz, yob.
* **output_format** (*str*) - (None) Format of output file. If not provided, file extension will be taken. Values: acesin, adf, alc, ascii, bgf, box, bs, c3d1, c3d2, cac, caccrt, cache, cacint, can, cdjson, cdxml, cht, cif, ck, cml, cmlr, com, confabreport, CONFIG, CONTCAR, CONTFF, copy, crk2d, crk3d, csr, cssr, ct, cub, cube, dalmol, dmol, dx, ent, exyz, fa, fasta, feat, fh, fhiaims, fix, fps, fpt, fract, fs, fsa, gamin, gau, gjc, gjf, gpr, gr96, gro, gukin, gukout, gzmat, hin, inchi, inchikey, inp, jin, k, lmpdat, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mna, mol, mol2, mold, molden, molf, molreport, mop, mopcrt, mopin, mp, mpc, mpd, mpqcin, mrv, msms, nul, nw, orcainp, outmol, paint, pcjson, pcm, pdb, pdbqt, png, pointcloud, POSCAR, POSFF, pov, pqr, pqs, qcin, report, rsmi, rxn, sd, sdf, smi, smiles, stl, svg, sy2, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xed, xyz, yob, zin.
* **coordinates** (*int*) - (None) Type of coordinates: 2D or 3D. Values: 2, 3.
* **ph** (*float*) - (None) Add hydrogens appropriate for pH.
* **obabel_path** (*str*) - ("obabel") Path to the obabel executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('informaticsmatters/obabel:latest') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML

#### Common file config


```python
properties:
  input_format: pdb
  output_format: pdb
  coordinates: 3
  ph: 7.4
```

#### Docker file config


```python
properties:
  input_format: pdb
  output_format: pdb
  coordinates: 3
  ph: 7.4
  container_path: docker
  container_image: informaticsmatters/obabel:latest
  container_volume_path: /tmp
```

#### Singularity file config


```python
properties:
  input_format: pdb
  output_format: pdb
  coordinates: 3
  ph: 7.4
  container_path: singularity
  container_image: shub://bioexcel/obabel_singularity
  container_volume_path: /tmp
```

#### Command line


```python
babel_add_hydrogens --config data/conf/add_hydrogens.yml --input_path data/input/babel.no.H.pdb --output_path data/output/output.add.H.pdb
```

### JSON

#### Common file config


```python
{
  "properties": {
    "input_format": "pdb",
    "output_format": "pdb",
    "coordinates": 3,
    "ph": 7.4
  }
}
```

#### Docker file config


```python
{
  "properties": {
    "input_format": "pdb",
    "output_format": "pdb",
    "coordinates": 3,
    "ph": 7.4,
    "container_path": "docker"
    "container_image": "informaticsmatters/obabel:latest"
    "container_volume_path": "/tmp"
  }
}
```

#### Singularity file config


```python
{
  "properties": {
    "input_format": "pdb",
    "output_format": "pdb",
    "coordinates": 3,
    "ph": 7.4,
    "container_path": "singularity"
    "container_image": "shub://bioexcel/obabel_singularity"
    "container_volume_path": "/tmp"
  }
}
```

#### Command line


```python
babel_add_hydrogens --config data/conf/add_hydrogens.json --input_path data/input/babel.no.H.pdb --output_path data/output/output.add.H.pdb
```

## Babel convert

Small molecule format conversion.

### Get help

Command:


```python
babel_convert -h
```


```python
usage: babel_convert [-h] [--config CONFIG] --input_path INPUT_PATH --output_path OUTPUT_PATH

Small molecule format conversion.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Configuration file

required arguments:
  --input_path INPUT_PATH
                        Path to the input file. Accepted formats: abinit, acesout, acr, adfout, alc, aoforce, arc, axsf, bgf, box, bs, c09out, c3d2, caccrt, can, car, castep, ccc, cdjson, cdx, cdxml, cif, ck, cml, cmlr, CONFIG, CONTCAR, CONTFF, crk2d, crk3d, ct, cub, cube, dallog, dalmol, dat, dmol, dx, ent, exyz, fa, fasta, fch, fchk, fck, feat, fhiaims, fract, fs, fsa, g03, g09, g92, g94, g98, gal, gam, gamess, gamin, gamout, got, gpr, gro, gukin, gukout, gzmat, hin, HISTORY, inchi, inp, ins, jin, jout, log, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mol, mol2, mold, molden, molf, moo, mop, mopcrt, mopin, mopout, mpc, mpo, mpqc, mrv, msi, nwo, orca, out, outmol, output, pc, pcjson, pcm, pdb, pdbqt, png, pos, POSCAR, POSFF, pqr, pqs, prep, pwscf, qcout, res, rsmi, rxn, sd, sdf, siesta, smi, smiles, smy, sy2, t41, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xml, xsf, xtc, xyz, yob.
  --output_path OUTPUT_PATH
                        Path to the output file. Accepted formats: acesin, adf, alc, ascii, bgf, box, bs, c3d1, c3d2, cac, caccrt, cache, cacint, can, cdjson, cdxml, cht, cif, ck, cml, cmlr, com, confabreport, CONFIG, CONTCAR, CONTFF, copy, crk2d, crk3d, csr, cssr, ct, cub, cube, dalmol, dmol, dx, ent, exyz, fa, fasta, feat, fh, fhiaims, fix, fps, fpt, fract, fs, fsa, gamin, gau, gjc, gjf, gpr, gr96, gro, gukin, gukout, gzmat, hin, inchi, inchikey, inp, jin, k, lmpdat, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mna, mol, mol2, mold, molden, molf, molreport, mop, mopcrt, mopin, mp, mpc, mpd, mpqcin, mrv, msms, nul, nw, orcainp, outmol, paint, pcjson, pcm, pdb, pdbqt, png, pointcloud, POSCAR, POSFF, pov, pqr, pqs, qcin, report, rsmi, rxn, sd, sdf, smi, smiles, stl, svg, sy2, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xed, xyz, yob, zin.
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_path** (*str*): Path to the input file. File type: input. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/babel/babel.smi). Accepted formats: abinit, acesout, acr, adfout, alc, aoforce, arc, axsf, bgf, box, bs, c09out, c3d2, caccrt, can, car, castep, ccc, cdjson, cdx, cdxml, cif, ck, cml, cmlr, CONFIG, CONTCAR, CONTFF, crk2d, crk3d, ct, cub, cube, dallog, dalmol, dat, dmol, dx, ent, exyz, fa, fasta, fch, fchk, fck, feat, fhiaims, fract, fs, fsa, g03, g09, g92, g94, g98, gal, gam, gamess, gamin, gamout, got, gpr, gro, gukin, gukout, gzmat, hin, HISTORY, inchi, inp, ins, jin, jout, log, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mol, mol2, mold, molden, molf, moo, mop, mopcrt, mopin, mopout, mpc, mpo, mpqc, mrv, msi, nwo, orca, out, outmol, output, pc, pcjson, pcm, pdb, pdbqt, png, pos, POSCAR, POSFF, pqr, pqs, prep, pwscf, qcout, res, rsmi, rxn, sd, sdf, siesta, smi, smiles, smy, sy2, t41, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xml, xsf, xtc, xyz, yob.
* **output_path** (*str*): Path to the output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/babel/ref_babel.convert.mol2). Accepted formats: acesin, adf, alc, ascii, bgf, box, bs, c3d1, c3d2, cac, caccrt, cache, cacint, can, cdjson, cdxml, cht, cif, ck, cml, cmlr, com, confabreport, CONFIG, CONTCAR, CONTFF, copy, crk2d, crk3d, csr, cssr, ct, cub, cube, dalmol, dmol, dx, ent, exyz, fa, fasta, feat, fh, fhiaims, fix, fps, fpt, fract, fs, fsa, gamin, gau, gjc, gjf, gpr, gr96, gro, gukin, gukout, gzmat, hin, inchi, inchikey, inp, jin, k, lmpdat, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mna, mol, mol2, mold, molden, molf, molreport, mop, mopcrt, mopin, mp, mpc, mpd, mpqcin, mrv, msms, nul, nw, orcainp, outmol, paint, pcjson, pcm, pdb, pdbqt, png, pointcloud, POSCAR, POSFF, pov, pqr, pqs, qcin, report, rsmi, rxn, sd, sdf, smi, smiles, stl, svg, sy2, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xed, xyz, yob, zin.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **input_format** (*str*) - (None) Format of input file. If not provided, file extension will be taken. Values: abinit, acesout, acr, adfout, alc, aoforce, arc, axsf, bgf, box, bs, c09out, c3d2, caccrt, can, car, castep, ccc, cdjson, cdx, cdxml, cif, ck, cml, cmlr, CONFIG, CONTCAR, CONTFF, crk2d, crk3d, ct, cub, cube, dallog, dalmol, dat, dmol, dx, ent, exyz, fa, fasta, fch, fchk, fck, feat, fhiaims, fract, fs, fsa, g03, g09, g92, g94, g98, gal, gam, gamess, gamin, gamout, got, gpr, gro, gukin, gukout, gzmat, hin, HISTORY, inchi, inp, ins, jin, jout, log, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mol, mol2, mold, molden, molf, moo, mop, mopcrt, mopin, mopout, mpc, mpo, mpqc, mrv, msi, nwo, orca, out, outmol, output, pc, pcjson, pcm, pdb, pdbqt, png, pos, POSCAR, POSFF, pqr, pqs, prep, pwscf, qcout, res, rsmi, rxn, sd, sdf, siesta, smi, smiles, smy, sy2, t41, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xml, xsf, xtc, xyz, yob.
* **output_format** (*str*) - (None) Format of output file. If not provided, file extension will be taken. Values: acesin, adf, alc, ascii, bgf, box, bs, c3d1, c3d2, cac, caccrt, cache, cacint, can, cdjson, cdxml, cht, cif, ck, cml, cmlr, com, confabreport, CONFIG, CONTCAR, CONTFF, copy, crk2d, crk3d, csr, cssr, ct, cub, cube, dalmol, dmol, dx, ent, exyz, fa, fasta, feat, fh, fhiaims, fix, fps, fpt, fract, fs, fsa, gamin, gau, gjc, gjf, gpr, gr96, gro, gukin, gukout, gzmat, hin, inchi, inchikey, inp, jin, k, lmpdat, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mna, mol, mol2, mold, molden, molf, molreport, mop, mopcrt, mopin, mp, mpc, mpd, mpqcin, mrv, msms, nul, nw, orcainp, outmol, paint, pcjson, pcm, pdb, pdbqt, png, pointcloud, POSCAR, POSFF, pov, pqr, pqs, qcin, report, rsmi, rxn, sd, sdf, smi, smiles, stl, svg, sy2, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xed, xyz, yob, zin.
* **coordinates** (*int*) - (None) Type of coordinates: 2D or 3D. Values: 2, 3.
* **ph** (*float*) - (None) Add hydrogens appropriate for pH.
* **obabel_path** (*str*) - ("obabel") Path to the obabel executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('informaticsmatters/obabel:latest') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML

#### Common file config


```python
properties:
  input_format: smi
  output_format: pdb
  coordinates: 2
  ph: 7.4
```

#### Docker file config


```python
properties:
  input_format: smi
  output_format: pdb
  coordinates: 2
  ph: 7.4
  container_path: docker
  container_image: informaticsmatters/obabel:latest
  container_volume_path: /tmp
```

#### Singularity file config


```python
properties:
  input_format: smi
  output_format: pdb
  coordinates: 2
  ph: 7.4
  container_path: singularity
  container_image: shub://bioexcel/obabel_singularity
  container_volume_path: /tmp
```

#### Command line


```python
babel_convert --config data/conf/convert.yml --input_path data/input/babel.smi --output_path data/output/output.convert.pdb
```

### JSON

#### Common  file config


```python
{
  "properties": {
    "input_format": "smi",
    "output_format": "pdb",
    "coordinates": 2,
    "ph": 7.4
  }
}
```

#### Docker  file config


```python
{
  "properties": {
    "input_format": "smi",
    "output_format": "pdb",
    "coordinates": 2,
    "ph": 7.4,
    "container_path": "docker"
    "container_image": "informaticsmatters/obabel:latest"
    "container_volume_path": "/tmp"
  }
}
```

#### Singularity  file config


```python
{
  "properties": {
    "input_format": "smi",
    "output_format": "pdb",
    "coordinates": 2,
    "ph": 7.4,
    "container_path": "singularity"
    "container_image": "shub://bioexcel/obabel_singularity"
    "container_volume_path": "/tmp"
  }
}
```

#### Command line


```python
babel_convert --config data/conf/convert.json --input_path data/input/babel.smi --output_path data/output/output.convert.pdb
```

## Babel minimize

Energetically minimize small molecules.

### Get help

Command:


```python
babel_minimize -h
```


```python
usage: babel_minimize [-h] [--config CONFIG] --input_path INPUT_PATH --output_path OUTPUT_PATH

Energetically minimize small molecules.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Configuration file

required arguments:
  --input_path INPUT_PATH
                        Path to the input file. Accepted formats: pdb, mol2.
  --output_path OUTPUT_PATH
                        Path to the output file. Accepted formats: pdb, mol2.
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_path** (*str*): Path to the input file. File type: input. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/babel/babel.minimize.pdb). Accepted formats: pdb, mol2.
* **output_path** (*str*): Path to the output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/babel/ref_babel.minimize.pdb). Accepted formats: pdb, mol2.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **criteria** (*float*) - (1e-6) Convergence criteria
* **method** (*str*) - ("cg") Method. Values: cg (conjugate gradients algorithm), sd (steepest descent algorithm).
* **force_field** (*str*) - (None) Force field. Values: GAFF (General Amber Force Field), Ghemical (Ghemical force field), MMFF94 (MMFF94 force field), MMFF94s (MMFF94s force field), UFF (Universal Force Field).
* **hydrogens** (*bool*) - (False) Add hydrogen atoms.
* **steps** (*int*) - (2500) Maximum number of steps.
* **cutoff** (*bool*) - (False) Use cut-off.
* **rvdw** (*float*) - (6.0) VDW cut-off distance.
* **rele** (*float*) - (10.0) Electrostatic cut-off distance.
* **frequency** (*int*) - (10) Frequency to update the non-bonded pairs.
* **obminimize_path** (*str*) - ("obminimize") Path to the obminimize executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('informaticsmatters/obabel:latest') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML

#### Common file config


```python
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
```

#### Docker file config


```python
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
  container_path: docker
  container_image: informaticsmatters/obabel:latest
  container_volume_path: /tmp
```

#### Singularity file config


```python
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
  container_path: singularity
  container_image: shub://bioexcel/obabel_singularity
  container_volume_path: /tmp
```

#### Command line


```python
babel_minimize --config data/conf/minimize.yml --input_path data/input/babel.minimize.pdb --output_path data/output/output.minimize.pdb
```

### JSON

#### Common file config


```python
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
```

#### Docker file config


```python
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
    "frequency": 10,
    "container_path": "docker"
    "container_image": "informaticsmatters/obabel:latest"
    "container_volume_path": "/tmp"
  }
}
```

#### Singularity file config


```python
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
    "frequency": 10,
    "container_path": "singularity"
    "container_image": "shub://bioexcel/obabel_singularity"
    "container_volume_path": "/tmp"
  }
}
```

#### Command line


```python
babel_minimize --config data/conf/minimize.json --input_path data/input/babel.minimize.pdb --output_path data/output/output.minimize.pdb
```

## Babel remove hydrogens

Removes hydrogen atoms to small molecules.

### Get help

Command:


```python
babel_remove_hydrogens -h
```


```python
usage: babel_remove_hydrogens [-h] [--config CONFIG] --input_path INPUT_PATH --output_path OUTPUT_PATH

Removes hydrogen atoms to small molecules.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Configuration file

required arguments:
  --input_path INPUT_PATH
                        Path to the input file. Accepted formats: abinit, acesout, acr, adfout, alc, aoforce, arc, axsf, bgf, box, bs, c09out, c3d2, caccrt, can, car, castep, ccc, cdjson, cdx, cdxml, cif, ck, cml, cmlr, CONFIG, CONTCAR, CONTFF, crk2d, crk3d, ct, cub, cube, dallog, dalmol, dat, dmol, dx, ent, exyz, fa, fasta, fch, fchk, fck, feat, fhiaims, fract, fs, fsa, g03, g09, g92, g94, g98, gal, gam, gamess, gamin, gamout, got, gpr, gro, gukin, gukout, gzmat, hin, HISTORY, inchi, inp, ins, jin, jout, log, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mol, mol2, mold, molden, molf, moo, mop, mopcrt, mopin, mopout, mpc, mpo, mpqc, mrv, msi, nwo, orca, out, outmol, output, pc, pcjson, pcm, pdb, pdbqt, png, pos, POSCAR, POSFF, pqr, pqs, prep, pwscf, qcout, res, rsmi, rxn, sd, sdf, siesta, smi, smiles, smy, sy2, t41, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xml, xsf, xtc, xyz, yob.
  --output_path OUTPUT_PATH
                        Path to the output file. Accepted formats: acesin, adf, alc, ascii, bgf, box, bs, c3d1, c3d2, cac, caccrt, cache, cacint, can, cdjson, cdxml, cht, cif, ck, cml, cmlr, com, confabreport, CONFIG, CONTCAR, CONTFF, copy, crk2d, crk3d, csr, cssr, ct, cub, cube, dalmol, dmol, dx, ent, exyz, fa, fasta, feat, fh, fhiaims, fix, fps, fpt, fract, fs, fsa, gamin, gau, gjc, gjf, gpr, gr96, gro, gukin, gukout, gzmat, hin, inchi, inchikey, inp, jin, k, lmpdat, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mna, mol, mol2, mold, molden, molf, molreport, mop, mopcrt, mopin, mp, mpc, mpd, mpqcin, mrv, msms, nul, nw, orcainp, outmol, paint, pcjson, pcm, pdb, pdbqt, png, pointcloud, POSCAR, POSFF, pov, pqr, pqs, qcin, report, rsmi, rxn, sd, sdf, smi, smiles, stl, svg, sy2, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xed, xyz, yob, zin.
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_path** (*str*): Path to the input file. File type: input. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/babel/babel.H.pdb). Accepted formats: abinit, acesout, acr, adfout, alc, aoforce, arc, axsf, bgf, box, bs, c09out, c3d2, caccrt, can, car, castep, ccc, cdjson, cdx, cdxml, cif, ck, cml, cmlr, CONFIG, CONTCAR, CONTFF, crk2d, crk3d, ct, cub, cube, dallog, dalmol, dat, dmol, dx, ent, exyz, fa, fasta, fch, fchk, fck, feat, fhiaims, fract, fs, fsa, g03, g09, g92, g94, g98, gal, gam, gamess, gamin, gamout, got, gpr, gro, gukin, gukout, gzmat, hin, HISTORY, inchi, inp, ins, jin, jout, log, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mol, mol2, mold, molden, molf, moo, mop, mopcrt, mopin, mopout, mpc, mpo, mpqc, mrv, msi, nwo, orca, out, outmol, output, pc, pcjson, pcm, pdb, pdbqt, png, pos, POSCAR, POSFF, pqr, pqs, prep, pwscf, qcout, res, rsmi, rxn, sd, sdf, siesta, smi, smiles, smy, sy2, t41, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xml, xsf, xtc, xyz, yob.
* **output_path** (*str*): Path to the output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/babel/ref_babel.nohydrogens.pdb). Accepted formats: acesin, adf, alc, ascii, bgf, box, bs, c3d1, c3d2, cac, caccrt, cache, cacint, can, cdjson, cdxml, cht, cif, ck, cml, cmlr, com, confabreport, CONFIG, CONTCAR, CONTFF, copy, crk2d, crk3d, csr, cssr, ct, cub, cube, dalmol, dmol, dx, ent, exyz, fa, fasta, feat, fh, fhiaims, fix, fps, fpt, fract, fs, fsa, gamin, gau, gjc, gjf, gpr, gr96, gro, gukin, gukout, gzmat, hin, inchi, inchikey, inp, jin, k, lmpdat, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mna, mol, mol2, mold, molden, molf, molreport, mop, mopcrt, mopin, mp, mpc, mpd, mpqcin, mrv, msms, nul, nw, orcainp, outmol, paint, pcjson, pcm, pdb, pdbqt, png, pointcloud, POSCAR, POSFF, pov, pqr, pqs, qcin, report, rsmi, rxn, sd, sdf, smi, smiles, stl, svg, sy2, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xed, xyz, yob, zin.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **input_format** (*str*) - (None) Format of input file. If not provided, file extension will be taken. Values: abinit, acesout, acr, adfout, alc, aoforce, arc, axsf, bgf, box, bs, c09out, c3d2, caccrt, can, car, castep, ccc, cdjson, cdx, cdxml, cif, ck, cml, cmlr, CONFIG, CONTCAR, CONTFF, crk2d, crk3d, ct, cub, cube, dallog, dalmol, dat, dmol, dx, ent, exyz, fa, fasta, fch, fchk, fck, feat, fhiaims, fract, fs, fsa, g03, g09, g92, g94, g98, gal, gam, gamess, gamin, gamout, got, gpr, gro, gukin, gukout, gzmat, hin, HISTORY, inchi, inp, ins, jin, jout, log, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mol, mol2, mold, molden, molf, moo, mop, mopcrt, mopin, mopout, mpc, mpo, mpqc, mrv, msi, nwo, orca, out, outmol, output, pc, pcjson, pcm, pdb, pdbqt, png, pos, POSCAR, POSFF, pqr, pqs, prep, pwscf, qcout, res, rsmi, rxn, sd, sdf, siesta, smi, smiles, smy, sy2, t41, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xml, xsf, xtc, xyz, yob.
* **output_format** (*str*) - (None) Format of output file. If not provided, file extension will be taken. Values: acesin, adf, alc, ascii, bgf, box, bs, c3d1, c3d2, cac, caccrt, cache, cacint, can, cdjson, cdxml, cht, cif, ck, cml, cmlr, com, confabreport, CONFIG, CONTCAR, CONTFF, copy, crk2d, crk3d, csr, cssr, ct, cub, cube, dalmol, dmol, dx, ent, exyz, fa, fasta, feat, fh, fhiaims, fix, fps, fpt, fract, fs, fsa, gamin, gau, gjc, gjf, gpr, gr96, gro, gukin, gukout, gzmat, hin, inchi, inchikey, inp, jin, k, lmpdat, lpmd, mcdl, mcif, MDFF, mdl, ml2, mmcif, mmd, mmod, mna, mol, mol2, mold, molden, molf, molreport, mop, mopcrt, mopin, mp, mpc, mpd, mpqcin, mrv, msms, nul, nw, orcainp, outmol, paint, pcjson, pcm, pdb, pdbqt, png, pointcloud, POSCAR, POSFF, pov, pqr, pqs, qcin, report, rsmi, rxn, sd, sdf, smi, smiles, stl, svg, sy2, tdd, text, therm, tmol, txt, txyz, unixyz, VASP, vmol, xed, xyz, yob, zin.
* **coordinates** (*int*) - (None) Type of coordinates: 2D or 3D. Values: 2, 3.
* **ph** (*float*) - (None) Add hydrogens appropriate for pH.
* **obabel_path** (*str*) - ("obabel") Path to the obabel executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('informaticsmatters/obabel:latest') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML

#### Common file config


```python
properties:
  input_format: pdb
  output_format: pdb
  coordinates: 3
  ph: 7.4
```

#### Docker file config


```python
properties:
  input_format: pdb
  output_format: pdb
  coordinates: 3
  ph: 7.4
  container_path: docker
  container_image: informaticsmatters/obabel:latest
  container_volume_path: /tmp
```

#### Singularity file config


```python
properties:
  input_format: pdb
  output_format: pdb
  coordinates: 3
  ph: 7.4
  container_path: singularity
  container_image: shub://bioexcel/obabel_singularity
  container_volume_path: /tmp
```

#### Command line


```python
babel_remove_hydrogens --config data/conf/remove_hydrogens.yml --input_path data/input/babel.H.pdb --output_path data/output/output.remove.H.pdb
```

### JSON

#### Common file config


```python
{
  "properties": {
    "input_format": "pdb",
    "output_format": "pdb",
    "coordinates": 3,
    "ph": 7.4
  }
}
```

#### Docker file config


```python
{
  "properties": {
    "input_format": "pdb",
    "output_format": "pdb",
    "coordinates": 3,
    "ph": 7.4,
    "container_path": "docker"
    "container_image": "informaticsmatters/obabel:latest"
    "container_volume_path": "/tmp"
  }
}
```

#### Singularity file config


```python
{
  "properties": {
    "input_format": "pdb",
    "output_format": "pdb",
    "coordinates": 3,
    "ph": 7.4,
    "container_path": "singularity"
    "container_image": "shub://bioexcel/obabel_singularity"
    "container_volume_path": "/tmp"
  }
}
```

#### Command line


```python
babel_remove_hydrogens --config data/conf/remove_hydrogens.json --input_path data/input/babel.H.pdb --output_path data/output/output.remove.H.pdb
```

## Reduce add hydrogens

Adds hydrogen atoms to small molecules.

### Get help

Command:


```python
reduce_add_hydrogens -h
```


```python
usage: reduce_add_hydrogens [-h] [--config CONFIG] --input_path INPUT_PATH --output_path OUTPUT_PATH

Adds hydrogen atoms to small molecules.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Configuration file

required arguments:
  --input_path INPUT_PATH
                        Path to the input file. Accepted formats: pdb.
  --output_path OUTPUT_PATH
                        Path to the output file. Accepted formats: pdb.
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_path** (*str*): Path to the input file. File type: input. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/ambertools/reduce.no.H.pdb). Accepted formats: pdb.
* **output_path** (*str*): Path to the output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/ambertools/ref_reduce.add.pdb). Accepted formats: pdb.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **flip** (*Boolean*) - (False) add H and rotate and flip NQH groups
* **noflip** (*Boolean*) - (False) add H and rotate groups with no NQH flips
* **nuclear** (*Boolean*) - (False) use nuclear X-H distances rather than default electron cloud distances
* **nooh** (*Boolean*) - (False) remove hydrogens on OH and SH groups
* **oh** (*Boolean*) - (True) add hydrogens on OH and SH groups (default)
* **his** (*Boolean*) - (False) create NH hydrogens on HIS rings (usually used with -HIS)
* **noheth** (*Boolean*) - (False) do not attempt to add NH proton on Het groups
* **rotnh3** (*Boolean*) - (True) allow lysine NH3 to rotate (default)
* **norotnh3** (*Boolean*) - (False) do not allow lysine NH3 to rotate
* **rotexist** (*Boolean*) - (False) allow existing rotatable groups (OH, SH, Met-CH3) to rotate
* **rotexoh** (*Boolean*) - (False) allow existing OH & SH groups to rotate
* **allalt** (*Boolean*) - (True) process adjustments for all conformations (default)
* **onlya** (*Boolean*) - (False) only adjust 'A' conformations
* **charges** (*Boolean*) - (False) output charge state for appropriate hydrogen records
* **dorotmet** (*Boolean*) - (False) allow methionine methyl groups to rotate (not recommended)
* **noadjust** (*Boolean*) - (False) do not process any rot or flip adjustments
* **build** (*Boolean*) - (False) add H, including His sc NH, then rotate and flip groups (except for pre-existing methionine methyl hydrogens)
* **reduce_path** (*str*) - ("reduce") Path to the reduce executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('afandiadib/ambertools:serial') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML

#### Common file config


```python
properties:
  nooh: True
```

#### Docker file config


```python
properties:
  nooh: True
  container_path: docker
  container_image: afandiadib/ambertools:serial
  container_volume_path: /tmp
```

#### Singularity file config


```python
properties:
  nooh: True
  container_path: singularity
  container_image: shub://bioexcel/ambertools_singularity
  container_volume_path: /tmp
```

#### Command line


```python
reduce_add_hydrogens --config data/conf/reduce_add_hydrogens.yml --input_path data/input/reduce.no.H.pdb --output_path data/output/output.reduce.H.pdb
```

### JSON

#### Common file config


```python
{
  "properties": {
    "nooh": true
  }
}
```

#### Docker file config


```python
{
  "properties": {
    "nooh": true,
    "container_path": "docker",
    "container_image": "afandiadib/ambertools:serial",
    "container_volume_path": "/tmp"
  }
}
```

#### Singularity file config


```python
{
  "properties": {
    "nooh": true,
    "container_path": "singularity",
    "container_image": "shub://bioexcel/ambertools_singularity",
    "container_volume_path": "/tmp"
  }
}
```

#### Command line


```python
reduce_add_hydrogens --config data/conf/reduce_add_hydrogens.json --input_path data/input/reduce.no.H.pdb --output_path data/output/output.reduce.H.pdb
```

## Reduce remove hydrogens

Removes hydrogen atoms to small molecules.

### Get help

Command:


```python
reduce_remove_hydrogens -h
```


```python
usage: reduce_remove_hydrogens [-h] [--config CONFIG] --input_path INPUT_PATH --output_path OUTPUT_PATH

Removes hydrogen atoms to small molecules.

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       Configuration file

required arguments:
  --input_path INPUT_PATH
                        Path to the input file. Accepted formats: pdb.
  --output_path OUTPUT_PATH
                        Path to the output file. Accepted formats: pdb.
```

### I / O Arguments

Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:

* **input_path** (*str*): Path to the input file. File type: input. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/ambertools/reduce.H.pdb). Accepted formats: pdb.
* **output_path** (*str*): Path to the output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/ambertools/ref_reduce.remove.pdb). Accepted formats: pdb.

### Config

Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:

* **reduce_path** (*str*) - ("reduce") Path to the reduce executable binary.
* **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
* **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
* **container_path** (*string*) - (None) Container path definition.
* **container_image** (*string*) - ('afandiadib/ambertools:serial') Container image definition.
* **container_volume_path** (*string*) - ('/tmp') Container volume path definition.
* **container_working_dir** (*string*) - (None) Container working directory definition.
* **container_user_id** (*string*) - (None) Container user_id definition.
* **container_shell_path** (*string*) - ('/bin/bash') Path to default shell inside the container.

### YAML

#### Common file config


```python
properties:
  reduce_path: "reduce"
```

#### Docker file config


```python
properties:
  reduce_path: "reduce"
  container_path: docker
  container_image: afandiadib/ambertools:serial
  container_volume_path: /tmp
```

#### Singularity file config


```python
properties:
  reduce_path: "reduce"
  container_path: singularity
  container_image: shub://bioexcel/ambertools_singularity
  container_volume_path: /tmp
```

#### Command line


```python
reduce_remove_hydrogens --config data/conf/reduce_remove_hydrogens.yml --input_path data/input/reduce.H.pdb --output_path data/output/output.reduce.pdb
```

### JSON

#### Common file config


```python
{
  "properties": {
    "reduce_path": "reduce"
  }
}
```

#### Docker file config


```python
{
  "properties": {
    "reduce_path": "reduce",
    "container_path": "docker",
    "container_image": "afandiadib/ambertools:serial",
    "container_volume_path": "/tmp"
  }
}
```

#### Singularity file config


```python
{
  "properties": {
    "reduce_path": "reduce",
    "container_path": "singularity",
    "container_image": "shub://bioexcel/ambertools_singularity",
    "container_volume_path": "/tmp"
  }
}
```

#### Command line


```python
reduce_remove_hydrogens --config data/conf/reduce_remove_hydrogens.json --input_path data/input/reduce.H.pdb --output_path data/output/output.reduce.pdb
```
