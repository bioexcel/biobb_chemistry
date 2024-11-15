# Biobb Chemistry changelog

## What's new in version [5.0.3](https://github.com/bioexcel/biobb_chemistry/releases/tag/v5.0.3)?

### Changes

* [FIX](all): Accept lists in different formats on input properties.

## What's new in version [5.0.2](https://github.com/bioexcel/biobb_chemistry/releases/tag/v5.0.2)?

### Changes
* [FEATURE](all): AcpypeConvertAMBERtoGMX module


## What's new in version [5.0.0](https://github.com/bioexcel/biobb_chemistry/releases/tag/v5.0.0)?

### Changes

* [FEATURE](__init__): Importing submodules when a module is loaded

## What's new in version [4.2.1](https://github.com/bioexcel/biobb_chemistry/releases/tag/v4.2.1)?
In version 4.2.1 some improvements have been introduced in the babel tools.

### New features

* New properties in BabelAddHydrogens (babel)
* New properties in BabelConvert (babel)
* New properties in BabelRemoveHydrogens (babel)

## What's new in version [4.2.0](https://github.com/bioexcel/biobb_chemistry/releases/tag/v4.2.0)?
In version 4.2.0 the dependency biobb_common has been updated to 4.2.0 version.

### New features

* Update to biobb_common 4.2.0 (general)
* Minor bug fixes in BabelAddHydrogens (babel)

## What's new in version [4.1.0](https://github.com/bioexcel/biobb_chemistry/releases/tag/v4.1.0)?
In version 4.1.0 the dependency biobb_common has been updated to 4.1.0 version.

### New features

* Update to biobb_common 4.1.0 (general)

## What's new in version [4.0.0](https://github.com/bioexcel/biobb_chemistry/releases/tag/v4.0.0)?
In version 4.0.0 the dependency biobb_common has been updated to 4.0.0 version.

### New features

* Update to biobb_common 4.0.0 (general)

## What's new in version [3.9.0](https://github.com/bioexcel/biobb_chemistry/releases/tag/v3.9.0)?
In version 3.9.0 the dependency biobb_common has been updated to 3.9.0 version.

### New features

* Update to biobb_common 3.9.0 (general)
* All inputs/outputs are checked for correct file format, extension and type (general)

## What's new in version [3.8.0](https://github.com/bioexcel/biobb_chemistry/releases/tag/v3.8.0)?
In version 3.8.0 the dependency biobb_common has been updated to 3.8.1 version.

### New features

* Update to biobb_common 3.8.1 (general)

## What's new in version [3.7.0](https://github.com/bioexcel/biobb_chemistry/releases/tag/v3.7.0)?
In version 3.7.0 the dependency biobb_common has been updated to 3.7.0 version.

### New features

* Update to biobb_common 3.7.0 (general)

## What's new in version [3.6.0](https://github.com/bioexcel/biobb_chemistry/releases/tag/v3.6.0)?
In version 3.6.0 the dependency biobb_common has been updated to 3.6.0 version.

### New features

* Update to biobb_common 3.6.0 (general)

## What's new in version [3.5.0](https://github.com/bioexcel/biobb_chemistry/releases/tag/v3.5.0)?
In version 3.5.0 the dependency biobb_common has been updated to 3.5.1 version. Also, there has been implemented the new version of docstrings, therefore the JSON Schemas have been modified.

### New features

* Update to biobb_common 3.5.1 (general)
* New extended and improved JSON schemas (Galaxy and CWL-compliant) (general)

### Other changes

* New docstrings

## What's new in version [3.0.2](https://github.com/bioexcel/biobb_chemistry/releases/tag/v3.0.2)?
In version 3.0.2 the dependency biobb_common has been updated to 3.0.1 version.

### New features

* Update to biobb_common 3.0.1

## What's new in version [3.0.1](https://github.com/bioexcel/biobb_chemistry/releases/tag/v3.0.1)?
In version 3.0.1 Ambertools has been updated from 19.10 to 20.0. Openbabel has been downgraded and fixed to 2.4.1. A new conda installation recipe has been introduced.

### New features

* Update to Ambertools 20.0 (ambertools module)
* Fixed to Openbabel 2.4.1 (babelm module)

### Bug fixes

* Fixed bugs in unittests for .itp, .lib and .prmtop files (unittests)

## What's new in version [3.0.0](https://github.com/bioexcel/biobb_chemistry/releases/tag/v3.0.0)?
In version 3.0.0 Python has been updated to version 3.7. Big changes in the documentation style and content. Finally a new conda installation recipe has been introduced.

### New features

* Update to Python 3.7 (general)
* New conda installer (installation)
* Adding type hinting for easier usage (API)
* Deprecating os.path in favour of pathlib.path (modules)
* New command line documentation (documentation)

### Other changes

* New documentation styles (documentation)