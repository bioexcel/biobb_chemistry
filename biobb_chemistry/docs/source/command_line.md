# BioBB CHEMISTRY Command Line Help
Generic usage:
```python
biobb_command [-h] --config CONFIG --input_file(s) <input_file(s)> --output_file <output_file>
```
-----------------


## Acpype_convert_amber_to_gmx
This class is a wrapper of Acpype tool for the conversion of AMBER topologies to GROMACS.
### Get help
Command:
```python
acpype_convert_amber_to_gmx -h
```
    usage: acpype_convert_amber_to_gmx [-h] [--config CONFIG] --input_crd_path INPUT_CRD_PATH --input_top_path INPUT_TOP_PATH --output_path_gro OUTPUT_PATH_GRO --output_path_top OUTPUT_PATH_TOP
    
    Small molecule parameterization for GROMACS MD package.
    
    options:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_crd_path INPUT_CRD_PATH
                            Path to the input coordinates file (AMBER crd). Accepted formats: inpcrd.
      --input_top_path INPUT_TOP_PATH
                            Path to the input topology file (AMBER ParmTop). Accepted formats: top, parmtop, prmtop.
      --output_path_gro OUTPUT_PATH_GRO
                            Path to the GRO output file. Accepted formats: gro.
      --output_path_top OUTPUT_PATH_TOP
                            Path to the TOP output file. Accepted formats: top.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_crd_path** (*string*): Path to the input coordinates file (AMBER crd). File type: input. [Sample file](https://raw.githubusercontent.com/bioexcel/biobb_chemistry/master/biobb_chemistry/test/data/acpype/acpype.coords.inpcrd). Accepted formats: INPCRD
* **input_top_path** (*string*): Path to the input topology file (AMBER ParmTop). File type: input. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/acpype/acpype.top.prmtop). Accepted formats: TOP, PARMTOP, PRMTOP
* **output_path_gro** (*string*): Path to the GRO output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.amber2gmx.gro). Accepted formats: GRO
* **output_path_top** (*string*): Path to the TOP output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.amber2gmx.top). Accepted formats: TOP
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **basename** (*string*): (BBB) A basename for the project (folder and output files)..
* **binary_path** (*string*): (acpype) Path to the acpype executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (acpype/acpype:2022.7.21) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_convert_amber_to_gmx.yml)
```python
properties:
  basename: BBB

```
#### Command line
```python
acpype_convert_amber_to_gmx --config config_acpype_convert_amber_to_gmx.yml --input_crd_path acpype.coords.inpcrd --input_top_path acpype.top.prmtop --output_path_gro ref_acpype.amber2gmx.gro --output_path_top ref_acpype.amber2gmx.top
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_convert_amber_to_gmx.json)
```python
{
  "properties": {
    "basename": "BBB"
  }
}
```
#### Command line
```python
acpype_convert_amber_to_gmx --config config_acpype_convert_amber_to_gmx.json --input_crd_path acpype.coords.inpcrd --input_top_path acpype.top.prmtop --output_path_gro ref_acpype.amber2gmx.gro --output_path_top ref_acpype.amber2gmx.top
```

## Acpype_params_ac
This class is a wrapper of Acpype tool for small molecule parameterization for AMBER MD package.
### Get help
Command:
```python
acpype_params_ac -h
```
    usage: acpype_params_ac [-h] [--config CONFIG] --input_path INPUT_PATH --output_path_frcmod OUTPUT_PATH_FRCMOD --output_path_inpcrd OUTPUT_PATH_INPCRD --output_path_lib OUTPUT_PATH_LIB --output_path_prmtop OUTPUT_PATH_PRMTOP
    
    Small molecule parameterization for AMBER MD package.
    
    options:
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
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_path** (*string*): Path to the input file. File type: input. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/acpype/acpype.params.mol2). Accepted formats: PDB, MDL, MOL2
* **output_path_frcmod** (*string*): Path to the FRCMOD output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.ac.frcmod). Accepted formats: FRCMOD
* **output_path_inpcrd** (*string*): Path to the INPCRD output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.ac.inpcrd). Accepted formats: INPCRD
* **output_path_lib** (*string*): Path to the LIB output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.ac.lib). Accepted formats: LIB
* **output_path_prmtop** (*string*): Path to the PRMTOP output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.ac.prmtop). Accepted formats: PRMTOP
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **basename** (*string*): (BBB) A basename for the project (folder and output files)..
* **charge** (*integer*): (0) Net molecular charge, for gas default is 0. If None the charge is guessed by acpype..
* **binary_path** (*string*): (acpype) Path to the acpype executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (acpype/acpype:2022.7.21) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_ac.yml)
```python
properties:
  basename: BBB
  charge: 0

```
#### [Docker config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_ac_docker.yml)
```python
properties:
  basename: BBB
  charge: 0
  container_image: acpype/acpype:2022.7.21
  container_path: docker
  container_volume_path: /tmp

```
#### [Singularity config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_ac_singularity.yml)
```python
properties:
  basename: BBB
  charge: 0
  container_image: shub://bioexcel/acpype_container
  container_path: singularity
  container_shell_path: /bin/sh
  container_volume_path: /tmp
  container_working_dir: /tmp

```
#### Command line
```python
acpype_params_ac --config config_acpype_params_ac.yml --input_path acpype.params.mol2 --output_path_frcmod ref_acpype.ac.frcmod --output_path_inpcrd ref_acpype.ac.inpcrd --output_path_lib ref_acpype.ac.lib --output_path_prmtop ref_acpype.ac.prmtop
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_ac.json)
```python
{
  "properties": {
    "basename": "BBB",
    "charge": 0
  }
}
```
#### [Docker config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_ac_docker.json)
```python
{
  "properties": {
    "basename": "BBB",
    "charge": 0,
    "container_path": "docker",
    "container_image": "acpype/acpype:2022.7.21",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_ac_singularity.json)
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
acpype_params_ac --config config_acpype_params_ac.json --input_path acpype.params.mol2 --output_path_frcmod ref_acpype.ac.frcmod --output_path_inpcrd ref_acpype.ac.inpcrd --output_path_lib ref_acpype.ac.lib --output_path_prmtop ref_acpype.ac.prmtop
```

## Acpype_params_cns
This class is a wrapper of Acpype tool for small molecule parameterization for CNS/XPLOR MD package.
### Get help
Command:
```python
acpype_params_cns -h
```
    usage: acpype_params_cns [-h] [--config CONFIG] --input_path INPUT_PATH --output_path_par OUTPUT_PATH_PAR --output_path_inp OUTPUT_PATH_INP --output_path_top OUTPUT_PATH_TOP --output_path_pdb OUTPUT_PATH_PDB
    
    Small molecule parameterization for CNS/XPLOR MD package.
    
    options:
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
      --output_path_pdb OUTPUT_PATH_PDB
                            Path to the PDB output file. Accepted formats: pdb.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_path** (*string*): Path to the input file. File type: input. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/acpype/acpype.params.mol2). Accepted formats: PDB, MDL, MOL2
* **output_path_par** (*string*): Path to the PAR output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.cns.par). Accepted formats: PAR
* **output_path_inp** (*string*): Path to the INP output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.cns.inp). Accepted formats: INP
* **output_path_top** (*string*): Path to the TOP output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.cns.top). Accepted formats: TOP
* **output_path_pdb** (*string*): Path to the PDB output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.cns.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **basename** (*string*): (BBB) A basename for the project (folder and output files)..
* **charge** (*integer*): (0) Net molecular charge, for gas default is 0. If None the charge is guessed by acpype..
* **binary_path** (*string*): (acpype) Path to the acpype executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (acpype/acpype:2022.7.21) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_cns.yml)
```python
properties:
  basename: BBB
  charge: 0

```
#### [Docker config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_cns_docker.yml)
```python
properties:
  basename: BBB
  charge: 0
  container_image: acpype/acpype:2022.7.21
  container_path: docker
  container_volume_path: /tmp

```
#### [Singularity config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_cns_singularity.yml)
```python
properties:
  basename: BBB
  charge: 0
  container_image: shub://bioexcel/acpype_container
  container_path: singularity
  container_shell_path: /bin/sh
  container_volume_path: /tmp
  container_working_dir: /tmp

```
#### Command line
```python
acpype_params_cns --config config_acpype_params_cns.yml --input_path acpype.params.mol2 --output_path_par ref_acpype.cns.par --output_path_inp ref_acpype.cns.inp --output_path_top ref_acpype.cns.top --output_path_pdb ref_acpype.cns.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_cns.json)
```python
{
  "properties": {
    "basename": "BBB",
    "charge": 0
  }
}
```
#### [Docker config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_cns_docker.json)
```python
{
  "properties": {
    "basename": "BBB",
    "charge": 0,
    "container_path": "docker",
    "container_image": "acpype/acpype:2022.7.21",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_cns_singularity.json)
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
acpype_params_cns --config config_acpype_params_cns.json --input_path acpype.params.mol2 --output_path_par ref_acpype.cns.par --output_path_inp ref_acpype.cns.inp --output_path_top ref_acpype.cns.top --output_path_pdb ref_acpype.cns.pdb
```

## Acpype_params_gmx
This class is a wrapper of Acpype tool for generation of topologies for GROMACS.
### Get help
Command:
```python
acpype_params_gmx -h
```
    usage: acpype_params_gmx [-h] [--config CONFIG] --input_path INPUT_PATH --output_path_gro OUTPUT_PATH_GRO --output_path_itp OUTPUT_PATH_ITP --output_path_top OUTPUT_PATH_TOP
    
    Small molecule parameterization for GROMACS MD package.
    
    options:
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
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_path** (*string*): Path to the input file. File type: input. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/acpype/acpype.params.mol2). Accepted formats: PDB, MDL, MOL2
* **output_path_gro** (*string*): Path to the GRO output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.gmx.gro). Accepted formats: GRO
* **output_path_itp** (*string*): Path to the ITP output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.gmx.itp). Accepted formats: ITP
* **output_path_top** (*string*): Path to the TOP output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.gmx.top). Accepted formats: TOP
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **basename** (*string*): (BBB) A basename for the project (folder and output files)..
* **charge** (*integer*): (0) Net molecular charge, for gas default is 0. If None the charge is guessed by acpype..
* **binary_path** (*string*): (acpype) Path to the acpype executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (acpype/acpype:2022.7.21) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_gmx.yml)
```python
properties:
  basename: BBB
  charge: 0

```
#### [Docker config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_gmx_docker.yml)
```python
properties:
  basename: BBB
  charge: 0
  container_image: acpype/acpype:2022.7.21
  container_path: docker
  container_volume_path: /tmp

```
#### [Singularity config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_gmx_singularity.yml)
```python
properties:
  basename: BBB
  charge: 0
  container_image: shub://bioexcel/acpype_container
  container_path: singularity
  container_shell_path: /bin/sh
  container_volume_path: /tmp
  container_working_dir: /tmp

```
#### Command line
```python
acpype_params_gmx --config config_acpype_params_gmx.yml --input_path acpype.params.mol2 --output_path_gro ref_acpype.gmx.gro --output_path_itp ref_acpype.gmx.itp --output_path_top ref_acpype.gmx.top
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_gmx.json)
```python
{
  "properties": {
    "basename": "BBB",
    "charge": 0
  }
}
```
#### [Docker config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_gmx_docker.json)
```python
{
  "properties": {
    "basename": "BBB",
    "charge": 0,
    "container_path": "docker",
    "container_image": "acpype/acpype:2022.7.21",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_gmx_singularity.json)
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
acpype_params_gmx --config config_acpype_params_gmx.json --input_path acpype.params.mol2 --output_path_gro ref_acpype.gmx.gro --output_path_itp ref_acpype.gmx.itp --output_path_top ref_acpype.gmx.top
```

## Acpype_params_gmx_opls
This class is a wrapper of Acpype tool for generation of topologies for OPLS/AA.
### Get help
Command:
```python
acpype_params_gmx_opls -h
```
    usage: acpype_params_gmx_opls [-h] [--config CONFIG] --input_path INPUT_PATH --output_path_itp OUTPUT_PATH_ITP --output_path_top OUTPUT_PATH_TOP
    
    Small molecule parameterization for OPLS/AA MD package.
    
    options:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_path INPUT_PATH
                            Path to the input file. Accepted formats: pdb, mdl, mol2.
      --output_path_itp OUTPUT_PATH_ITP
                            Path to the ITP output file. Accepted formats: itp.
      --output_path_top OUTPUT_PATH_TOP
                            Path to the TOP output file. Accepted formats: top.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_path** (*string*): Path to the input file. File type: input. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/acpype/acpype.params.mol2). Accepted formats: PDB, MDL, MOL2
* **output_path_itp** (*string*): Path to the ITP output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.gmx.opls.itp). Accepted formats: ITP
* **output_path_top** (*string*): Path to the TOP output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/acpype/ref_acpype.gmx.opls.top). Accepted formats: TOP
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **basename** (*string*): (BBB) A basename for the project (folder and output files)..
* **charge** (*integer*): (0) Net molecular charge, for gas default is 0. If None the charge is guessed by acpype..
* **binary_path** (*string*): (acpype) Path to the acpype executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (acpype/acpype:2022.7.21) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_gmx_opls.yml)
```python
properties:
  basename: BBB
  charge: 0

```
#### [Docker config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_gmx_opls_docker.yml)
```python
properties:
  basename: BBB
  charge: 0
  container_image: acpype/acpype:2022.7.21
  container_path: docker
  container_volume_path: /tmp

```
#### [Singularity config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_gmx_opls_singularity.yml)
```python
properties:
  basename: BBB
  charge: 0
  container_image: shub://bioexcel/acpype_container
  container_path: singularity
  container_shell_path: /bin/sh
  container_volume_path: /tmp
  container_working_dir: /tmp

```
#### Command line
```python
acpype_params_gmx_opls --config config_acpype_params_gmx_opls.yml --input_path acpype.params.mol2 --output_path_itp ref_acpype.gmx.opls.itp --output_path_top ref_acpype.gmx.opls.top
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_gmx_opls.json)
```python
{
  "properties": {
    "basename": "BBB",
    "charge": 0
  }
}
```
#### [Docker config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_gmx_opls_docker.json)
```python
{
  "properties": {
    "basename": "BBB",
    "charge": 0,
    "container_path": "docker",
    "container_image": "acpype/acpype:2022.7.21",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_acpype_params_gmx_opls_singularity.json)
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
acpype_params_gmx_opls --config config_acpype_params_gmx_opls.json --input_path acpype.params.mol2 --output_path_itp ref_acpype.gmx.opls.itp --output_path_top ref_acpype.gmx.opls.top
```

## Babel_add_hydrogens
This class is a wrapper of the Open Babel tool.
### Get help
Command:
```python
babel_add_hydrogens -h
```
    usage: babel_add_hydrogens [-h] [--config CONFIG] --input_path INPUT_PATH --output_path OUTPUT_PATH
    
    Adds hydrogen atoms to small molecules.
    
    options:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_path INPUT_PATH
                            Path to the input file. Accepted formats: dat, ent, fa, fasta, gro, inp, log, mcif, mdl, mmcif, mol, mol2, pdb, pdbqt, png, sdf, smi, smiles, txt, xml, xtc.
      --output_path OUTPUT_PATH
                            Path to the output file. Accepted formats: ent, fa, fasta, gro, inp, mcif, mdl, mmcif, mol, mol2, pdb, pdbqt, png, sdf, smi, smiles, txt.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_path** (*string*): Path to the input file. File type: input. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/babelm/babel.no.H.pdb). Accepted formats: DAT, ENT, FA, FASTA, GRO, INP, LOG, MCIF, MDL, MMCIF, MOL, MOL2, PDB, PDBQT, PNG, SDF, SMI, SMILES, TXT, XML, XTC
* **output_path** (*string*): Path to the output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/babelm/ref_babel.hydrogens.pdb). Accepted formats: ENT, FA, FASTA, GRO, INP, MCIF, MDL, MMCIF, MOL, MOL2, PDB, PDBQT, PNG, SDF, SMI, SMILES, TXT
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **input_format** (*string*): (None) Format of input file. If not provided, input_path extension will be taken. .
* **output_format** (*string*): (None) Format of output file. If not provided, output_path extension will be taken. .
* **fs_input** (*array*): (None) Format-specific input options. .
* **fs_output** (*array*): ([h]) Format-specific output options. .
* **coordinates** (*integer*): (None) Type of coordinates: 2D or 3D. .
* **effort** (*string*): (medium) Computational effort wanted to dedicate for the conformer generation coordinates calculations, only for 3D coordinates. .
* **ph** (*number*): (7.4) Add hydrogens appropriate for pH..
* **binary_path** (*string*): (obabel) Path to the obabel executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (informaticsmatters/obabel:latest) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_add_hydrogens.yml)
```python
properties:
  coordinates: 3
  input_format: pdb
  output_format: pdb
  ph: 7.4

```
#### [Docker config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_add_hydrogens_docker.yml)
```python
properties:
  container_image: informaticsmatters/obabel:latest
  container_path: docker
  container_volume_path: /tmp
  coordinates: 3
  input_format: pdb
  output_format: pdb
  ph: 7.4

```
#### [Singularity config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_add_hydrogens_singularity.yml)
```python
properties:
  container_image: shub://bioexcel/obabel_singularity
  container_path: singularity
  container_volume_path: /tmp
  coordinates: 3
  input_format: pdb
  output_format: pdb
  ph: 7.4

```
#### Command line
```python
babel_add_hydrogens --config config_babel_add_hydrogens.yml --input_path babel.no.H.pdb --output_path ref_babel.hydrogens.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_add_hydrogens.json)
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
#### [Docker config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_add_hydrogens_docker.json)
```python
{
  "properties": {
    "input_format": "pdb",
    "output_format": "pdb",
    "coordinates": 3,
    "ph": 7.4,
    "container_path": "docker",
    "container_image": "informaticsmatters/obabel:latest",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_add_hydrogens_singularity.json)
```python
{
  "properties": {
    "input_format": "pdb",
    "output_format": "pdb",
    "coordinates": 3,
    "ph": 7.4,
    "container_path": "singularity",
    "container_image": "shub://bioexcel/obabel_singularity",
    "container_volume_path": "/tmp"
  }
}
```
#### Command line
```python
babel_add_hydrogens --config config_babel_add_hydrogens.json --input_path babel.no.H.pdb --output_path ref_babel.hydrogens.pdb
```

## Babel_convert
This class is a wrapper of the Open Babel tool.
### Get help
Command:
```python
babel_convert -h
```
    usage: babel_convert [-h] [--config CONFIG] --input_path INPUT_PATH --output_path OUTPUT_PATH
    
    Small molecule format conversion.
    
    options:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_path INPUT_PATH
                            Path to the input file. Accepted formats: dat, ent, fa, fasta, gro, inp, log, mcif, mdl, mmcif, mol, mol2, pdb, pdbqt, png, sdf, smi, smiles, txt, xml, xtc.
      --output_path OUTPUT_PATH
                            Path to the output file. Accepted formats: ent, fa, fasta, gro, inp, mcif, mdl, mmcif, mol, mol2, pdb, pdbqt, png, sdf, smi, smiles, txt.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_path** (*string*): Path to the input file. File type: input. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/babelm/babel.smi). Accepted formats: DAT, ENT, FA, FASTA, GRO, INP, LOG, MCIF, MDL, MMCIF, MOL, MOL2, PDB, PDBQT, PNG, SDF, SMI, SMILES, TXT, XML, XTC
* **output_path** (*string*): Path to the output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/babelm/ref_babel.convert.mol2). Accepted formats: ENT, FA, FASTA, GRO, INP, MCIF, MDL, MMCIF, MOL, MOL2, PDB, PDBQT, PNG, SDF, SMI, SMILES, TXT
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **input_format** (*string*): (None) Format of input file. If not provided, input_path extension will be taken. .
* **output_format** (*string*): (None) Format of output file. If not provided, output_path extension will be taken. .
* **fs_input** (*array*): (None) Format-specific input options. .
* **fs_output** (*array*): (None) Format-specific output options. .
* **coordinates** (*integer*): (None) Type of coordinates: 2D or 3D. .
* **effort** (*string*): (medium) Computational effort wanted to dedicate for the conformer generation coordinates calculations, only for 3D coordinates. .
* **ph** (*number*): (7.4) Add hydrogens appropriate for pH..
* **flex** (*boolean*): (False) Remove all but the largest contiguous fragment (strip salts)..
* **binary_path** (*string*): (obabel) Path to the obabel executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (informaticsmatters/obabel:latest) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_convert.yml)
```python
properties:
  coordinates: 2
  input_format: smi
  output_format: mol2
  ph: 7.4

```
#### [Docker config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_convert_docker.yml)
```python
properties:
  container_image: informaticsmatters/obabel:latest
  container_path: docker
  container_volume_path: /tmp
  coordinates: 2
  input_format: smi
  output_format: mol2
  ph: 7.4

```
#### [Singularity config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_convert_singularity.yml)
```python
properties:
  container_image: shub://bioexcel/obabel_singularity
  container_path: singularity
  container_volume_path: /tmp
  coordinates: 2
  input_format: smi
  output_format: mol2
  ph: 7.4

```
#### Command line
```python
babel_convert --config config_babel_convert.yml --input_path babel.smi --output_path ref_babel.convert.mol2
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_convert.json)
```python
{
  "properties": {
    "input_format": "smi",
    "output_format": "mol2",
    "coordinates": 2,
    "ph": 7.4
  }
}
```
#### [Docker config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_convert_docker.json)
```python
{
  "properties": {
    "input_format": "smi",
    "output_format": "mol2",
    "coordinates": 2,
    "ph": 7.4,
    "container_path": "docker",
    "container_image": "informaticsmatters/obabel:latest",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_convert_singularity.json)
```python
{
  "properties": {
    "input_format": "smi",
    "output_format": "mol2",
    "coordinates": 2,
    "ph": 7.4,
    "container_path": "singularity",
    "container_image": "shub://bioexcel/obabel_singularity",
    "container_volume_path": "/tmp"
  }
}
```
#### Command line
```python
babel_convert --config config_babel_convert.json --input_path babel.smi --output_path ref_babel.convert.mol2
```

## Babel_minimize
This class is a wrapper of the Open Babel tool.
### Get help
Command:
```python
babel_minimize -h
```
    usage: babel_minimize [-h] [--config CONFIG] --input_path INPUT_PATH --output_path OUTPUT_PATH
    
    Energetically minimize small molecules.
    
    options:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_path INPUT_PATH
                            Path to the input file. Accepted formats: pdb, mol2.
      --output_path OUTPUT_PATH
                            Path to the output file. Accepted formats: pdb, mol2.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_path** (*string*): Path to the input file. File type: input. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/babelm/babel.minimize.pdb). Accepted formats: PDB, MOL2
* **output_path** (*string*): Path to the output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/babelm/ref_babel.minimize.pdb). Accepted formats: PDB, MOL2
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **criteria** (*number*): (1e-06) Convergence criteria.
* **method** (*string*): (cg) Method. .
* **force_field** (*string*): (None) Force field. .
* **hydrogens** (*boolean*): (False) Add hydrogen atoms..
* **steps** (*integer*): (2500) Maximum number of steps..
* **cutoff** (*boolean*): (False) Use cut-off..
* **rvdw** (*number*): (6.0) VDW cut-off distance..
* **rele** (*number*): (10.0) Electrostatic cut-off distance..
* **frequency** (*integer*): (10) Frequency to update the non-bonded pairs..
* **binary_path** (*string*): (obminimize) Path to the obminimize executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (informaticsmatters/obabel:latest) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_minimize.yml)
```python
properties:
  criteria: 1e-6
  cutoff: true
  force_field: GAFF
  frequency: 10
  hydrogens: true
  method: cg
  rele: 10.0
  rvdw: 6.0
  steps: 2500

```
#### [Docker config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_minimize_docker.yml)
```python
properties:
  container_image: informaticsmatters/obabel:latest
  container_path: docker
  container_volume_path: /tmp
  criteria: 1e-6
  cutoff: true
  force_field: GAFF
  frequency: 10
  hydrogens: true
  method: cg
  rele: 10.0
  rvdw: 6.0
  steps: 2500

```
#### [Singularity config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_minimize_singularity.yml)
```python
properties:
  container_image: shub://bioexcel/obabel_singularity
  container_path: singularity
  container_volume_path: /tmp
  criteria: 1e-6
  cutoff: true
  force_field: GAFF
  frequency: 10
  hydrogens: true
  method: cg
  rele: 10.0
  rvdw: 6.0
  steps: 2500

```
#### Command line
```python
babel_minimize --config config_babel_minimize.yml --input_path babel.minimize.pdb --output_path ref_babel.minimize.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_minimize.json)
```python
{
  "properties": {
    "criteria": "1e-6",
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
#### [Docker config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_minimize_docker.json)
```python
{
  "properties": {
    "criteria": "1e-6",
    "method": "cg",
    "force_field": "GAFF",
    "hydrogens": true,
    "steps": 2500,
    "cutoff": true,
    "rvdw": 6.0,
    "rele": 10.0,
    "frequency": 10,
    "container_path": "docker",
    "container_image": "informaticsmatters/obabel:latest",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_minimize_singularity.json)
```python
{
  "properties": {
    "criteria": "1e-6",
    "method": "cg",
    "force_field": "GAFF",
    "hydrogens": true,
    "steps": 2500,
    "cutoff": true,
    "rvdw": 6.0,
    "rele": 10.0,
    "frequency": 10,
    "container_path": "singularity",
    "container_image": "shub://bioexcel/obabel_singularity",
    "container_volume_path": "/tmp"
  }
}
```
#### Command line
```python
babel_minimize --config config_babel_minimize.json --input_path babel.minimize.pdb --output_path ref_babel.minimize.pdb
```

## Babel_remove_hydrogens
This class is a wrapper of the Open Babel tool.
### Get help
Command:
```python
babel_remove_hydrogens -h
```
    usage: babel_remove_hydrogens [-h] [--config CONFIG] --input_path INPUT_PATH --output_path OUTPUT_PATH
    
    Removes hydrogen atoms to small molecules.
    
    options:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_path INPUT_PATH
                            Path to the input file. Accepted formats: dat, ent, fa, fasta, gro, inp, log, mcif, mdl, mmcif, mol, mol2, pdb, pdbqt, png, sdf, smi, smiles, txt, xml, xtc.
      --output_path OUTPUT_PATH
                            Path to the output file. Accepted formats: ent, fa, fasta, gro, inp, mcif, mdl, mmcif, mol, mol2, pdb, pdbqt, png, sdf, smi, smiles, txt.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_path** (*string*): Path to the input file. File type: input. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/babelm/babel.H.pdb). Accepted formats: DAT, ENT, FA, FASTA, GRO, INP, LOG, MCIF, MDL, MMCIF, MOL, MOL2, PDB, PDBQT, PNG, SDF, SMI, SMILES, TXT, XML, XTC
* **output_path** (*string*): Path to the output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/babelm/ref_babel.nohydrogens.pdb). Accepted formats: ENT, FA, FASTA, GRO, INP, MCIF, MDL, MMCIF, MOL, MOL2, PDB, PDBQT, PNG, SDF, SMI, SMILES, TXT
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **input_format** (*string*): (None) Format of input file. If not provided, input_path extension will be taken. .
* **output_format** (*string*): (None) Format of output file. If not provided, output_path extension will be taken. .
* **fs_input** (*array*): (None) Format-specific input options. .
* **fs_output** (*array*): (None) Format-specific output options. .
* **coordinates** (*integer*): (None) Type of coordinates: 2D or 3D. .
* **effort** (*string*): (medium) Computational effort wanted to dedicate for the conformer generation coordinates calculations, only for 3D coordinates. .
* **ph** (*number*): (7.4) Add hydrogens appropriate for pH..
* **binary_path** (*string*): (obabel) Path to the obabel executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (informaticsmatters/obabel:latest) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_remove_hydrogens.yml)
```python
properties:
  coordinates: 3
  input_format: pdb
  output_format: pdb
  ph: 7.4

```
#### [Docker config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_remove_hydrogens_docker.yml)
```python
properties:
  container_image: informaticsmatters/obabel:latest
  container_path: docker
  container_volume_path: /tmp
  coordinates: 3
  input_format: pdb
  output_format: pdb
  ph: 7.4

```
#### [Singularity config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_remove_hydrogens_singularity.yml)
```python
properties:
  container_image: shub://bioexcel/obabel_singularity
  container_path: singularity
  container_volume_path: /tmp
  coordinates: 3
  input_format: pdb
  output_format: pdb
  ph: 7.4

```
#### Command line
```python
babel_remove_hydrogens --config config_babel_remove_hydrogens.yml --input_path babel.H.pdb --output_path ref_babel.nohydrogens.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_remove_hydrogens.json)
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
#### [Docker config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_remove_hydrogens_docker.json)
```python
{
  "properties": {
    "input_format": "pdb",
    "output_format": "pdb",
    "coordinates": 3,
    "ph": 7.4,
    "container_path": "docker",
    "container_image": "informaticsmatters/obabel:latest",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_babel_remove_hydrogens_singularity.json)
```python
{
  "properties": {
    "input_format": "pdb",
    "output_format": "pdb",
    "coordinates": 3,
    "ph": 7.4,
    "container_path": "singularity",
    "container_image": "shub://bioexcel/obabel_singularity",
    "container_volume_path": "/tmp"
  }
}
```
#### Command line
```python
babel_remove_hydrogens --config config_babel_remove_hydrogens.json --input_path babel.H.pdb --output_path ref_babel.nohydrogens.pdb
```

## Reduce_add_hydrogens
This class is a wrapper of the Ambertools reduce module for adding hydrogens to a given structure.
### Get help
Command:
```python
reduce_add_hydrogens -h
```
    usage: reduce_add_hydrogens [-h] [--config CONFIG] --input_path INPUT_PATH --output_path OUTPUT_PATH
    
    Adds hydrogen atoms to small molecules.
    
    options:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_path INPUT_PATH
                            Path to the input file. Accepted formats: pdb.
      --output_path OUTPUT_PATH
                            Path to the output file. Accepted formats: pdb.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_path** (*string*): Path to the input file. File type: input. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/ambertools/reduce.no.H.pdb). Accepted formats: PDB
* **output_path** (*string*): Path to the output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/ambertools/ref_reduce.add.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **flip** (*boolean*): (False) add H and rotate and flip NQH groups.
* **noflip** (*boolean*): (False) add H and rotate groups with no NQH flips.
* **nuclear** (*boolean*): (False) use nuclear X-H distances rather than default electron cloud distances.
* **nooh** (*boolean*): (False) remove hydrogens on OH and SH groups.
* **oh** (*boolean*): (True) add hydrogens on OH and SH groups (default).
* **his** (*boolean*): (False) create NH hydrogens on HIS rings (usually used with -HIS).
* **noheth** (*boolean*): (False) do not attempt to add NH proton on Het groups.
* **rotnh3** (*boolean*): (True) allow lysine NH3 to rotate (default).
* **norotnh3** (*boolean*): (False) do not allow lysine NH3 to rotate.
* **rotexist** (*boolean*): (False) allow existing rotatable groups (OH, SH, Met-CH3) to rotate.
* **rotexoh** (*boolean*): (False) allow existing OH & SH groups to rotate.
* **allalt** (*boolean*): (True) process adjustments for all conformations (default).
* **onlya** (*boolean*): (False) only adjust 'A' conformations.
* **charges** (*boolean*): (False) output charge state for appropriate hydrogen records.
* **dorotmet** (*boolean*): (False) allow methionine methyl groups to rotate (not recommended).
* **noadjust** (*boolean*): (False) do not process any rot or flip adjustments.
* **metal_bump** (*number*): (None) H 'bumps' metals at radius plus this.
* **non_metal_bump** (*number*): (None) 'bumps' nonmetal at radius plus this.
* **build** (*boolean*): (False) add H, including His sc NH, then rotate and flip groups (except for pre-existing methionine methyl hydrogens).
* **binary_path** (*string*): (reduce) Path to the reduce executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (afandiadib/ambertools:serial) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_reduce_add_hydrogens.yml)
```python
properties:
  nooh: true

```
#### [Docker config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_reduce_add_hydrogens_docker.yml)
```python
properties:
  container_image: afandiadib/ambertools:serial
  container_path: docker
  container_volume_path: /tmp
  nooh: true

```
#### [Singularity config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_reduce_add_hydrogens_singularity.yml)
```python
properties:
  container_image: shub://bioexcel/ambertools_singularity
  container_path: singularity
  container_volume_path: /tmp
  nooh: true

```
#### Command line
```python
reduce_add_hydrogens --config config_reduce_add_hydrogens.yml --input_path reduce.no.H.pdb --output_path ref_reduce.add.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_reduce_add_hydrogens.json)
```python
{
  "properties": {
    "nooh": true
  }
}
```
#### [Docker config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_reduce_add_hydrogens_docker.json)
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
#### [Singularity config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_reduce_add_hydrogens_singularity.json)
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
reduce_add_hydrogens --config config_reduce_add_hydrogens.json --input_path reduce.no.H.pdb --output_path ref_reduce.add.pdb
```

## Reduce_remove_hydrogens
This class is a wrapper of the Ambertools reduce module for removing hydrogens from a given structure.
### Get help
Command:
```python
reduce_remove_hydrogens -h
```
    usage: reduce_remove_hydrogens [-h] [--config CONFIG] --input_path INPUT_PATH --output_path OUTPUT_PATH
    
    Removes hydrogen atoms to small molecules.
    
    options:
      -h, --help            show this help message and exit
      --config CONFIG       Configuration file
    
    required arguments:
      --input_path INPUT_PATH
                            Path to the input file. Accepted formats: pdb.
      --output_path OUTPUT_PATH
                            Path to the output file. Accepted formats: pdb.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_path** (*string*): Path to the input file. File type: input. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/data/ambertools/reduce.H.pdb). Accepted formats: PDB
* **output_path** (*string*): Path to the output file. File type: output. [Sample file](https://github.com/bioexcel/biobb_chemistry/raw/master/biobb_chemistry/test/reference/ambertools/ref_reduce.remove.pdb). Accepted formats: PDB
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **binary_path** (*string*): (reduce) Path to the reduce executable binary..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory..
* **container_path** (*string*): (None) Container path definition..
* **container_image** (*string*): (afandiadib/ambertools:serial) Container image definition..
* **container_volume_path** (*string*): (/tmp) Container volume path definition..
* **container_working_dir** (*string*): (None) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_reduce_remove_hydrogens.yml)
```python
properties:
  remove_tmp: false

```
#### [Docker config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_reduce_remove_hydrogens_docker.yml)
```python
properties:
  container_image: afandiadib/ambertools:serial
  container_path: docker
  container_volume_path: /tmp

```
#### [Singularity config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_reduce_remove_hydrogens_singularity.yml)
```python
properties:
  container_image: shub://bioexcel/ambertools_singularity
  container_path: singularity
  container_volume_path: /tmp

```
#### Command line
```python
reduce_remove_hydrogens --config config_reduce_remove_hydrogens.yml --input_path reduce.H.pdb --output_path ref_reduce.remove.pdb
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_reduce_remove_hydrogens.json)
```python
{
  "properties": {
    "remove_tmp": false
  }
}
```
#### [Docker config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_reduce_remove_hydrogens_docker.json)
```python
{
  "properties": {
    "container_path": "docker",
    "container_image": "afandiadib/ambertools:serial",
    "container_volume_path": "/tmp"
  }
}
```
#### [Singularity config file](https://github.com/bioexcel/biobb_chemistry/blob/master/biobb_chemistry/test/data/config/config_reduce_remove_hydrogens_singularity.json)
```python
{
  "properties": {
    "container_path": "singularity",
    "container_image": "shub://bioexcel/ambertools_singularity",
    "container_volume_path": "/tmp"
  }
}
```
#### Command line
```python
reduce_remove_hydrogens --config config_reduce_remove_hydrogens.json --input_path reduce.H.pdb --output_path ref_reduce.remove.pdb
```
