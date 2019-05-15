""" Common functions for package biobb_chemistry.ambertools """
import os.path
import glob
import shutil
from biobb_common.tools import file_utils as fu

def check_input_path_reduce(path, classname):
	""" Checks input file """ 
	if not os.path.exists(path):
		raise SystemExit(classname + ': Unexisting input file')
	filename, file_extension = os.path.splitext(path)
	if not is_valid_pdb(file_extension[1:]):
		raise SystemExit(classname + ': Format %s in input file is not compatible' % file_extension[1:])

	return path

def check_output_path_reduce(path, classname):
	""" Checks output path """ 
	if os.path.dirname(path) and not os.path.exists(os.path.dirname(path)):
		raise SystemExit(classname + ': Unexisting output folder')
	filename, file_extension = os.path.splitext(path)
	if not is_valid_pdb(file_extension[1:]):
		raise SystemExit(classname + ': Format %s in input file is not compatible' % file_extension[1:])

	return path

def get_binary_path(properties, type):
	""" Gets binary path """
	return properties.get(type, get_default_value(type))


def get_default_value(key):
	""" Gives default values according to the given key """
	default_values = {
		"reduce_path": "reduce",
	}

	return default_values[key]

def is_valid_pdb(ext):
	""" Checks if input file format is compatible with Reduce """
	formats = ["pdb"]

	return ext in formats