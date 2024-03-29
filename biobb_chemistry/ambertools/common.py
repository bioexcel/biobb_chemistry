""" Common functions for package biobb_chemistry.ambertools """
from pathlib import Path, PurePath
from biobb_common.tools import file_utils as fu


def check_input_path(path, out_log, classname):
    """ Checks input file """
    if not Path(path).exists():
        fu.log(classname + ': Unexisting input file, exiting', out_log)
        raise SystemExit(classname + ': Unexisting input file')
    file_extension = PurePath(path).suffix
    if not is_valid_reduce(file_extension[1:]):
        fu.log(classname + ': Format %s in input file is not compatible' % file_extension[1:], out_log)
        raise SystemExit(classname + ': Format %s in input file is not compatible' % file_extension[1:])
    if (PurePath(path).name == path or not PurePath(path).is_absolute()):
        path = str(PurePath(Path.cwd()).joinpath(path))

    return path


def check_output_path(path, out_log, classname):
    """ Checks output path """
    if PurePath(path).parent and not Path(PurePath(path).parent).exists():
        fu.log(classname + ': Unexisting output %s output folder, exiting' % type, out_log)
        raise SystemExit(classname + ': Unexisting %s output folder' % type)
    file_extension = PurePath(path).suffix
    if not is_valid_reduce(file_extension[1:]):
        fu.log(classname + ': Format %s in input file is not compatible' % file_extension[1:], out_log)
        raise SystemExit(classname + ': Format %s in output file is not compatible' % file_extension[1:])

    return path


def get_binary_path(properties, type):
    """ Gets binary path """
    return properties.get(type, get_default_value(type))


def get_default_value(key):
    """ Gives default values according to the given key """
    default_values = {
        "binary_path": "reduce",
    }

    return default_values[key]


def is_valid_reduce(ext):
    """ Checks if input file format is compatible with Reduce """
    formats = ["pdb"]

    return ext in formats
