""" Common functions for package biobb_chemistry.acpype """
import os.path
import glob
import shutil
from biobb_common.tools import file_utils as fu

def check_input_path(path, out_log):
	""" Checks input file """ 
	if not os.path.exists(path):
		fu.log('Unexisting input file, exiting', out_log)
		raise SystemExit('Unexisting input file')
	filename, file_extension = os.path.splitext(path)
	if not is_valid_input(file_extension[1:]):
		fu.log('Format %s in input file is not compatible' % file_extension[1:], out_log)
		raise SystemExit('Format %s in input file is not compatible' % file_extension[1:])

	return path

def check_output_path(path, type, out_log):
	""" Checks output path """ 
	if not os.path.exists(os.path.dirname(path)):
		fu.log('Unexisting output %s output folder, exiting' % type, out_log)
		raise SystemExit('Unexisting %s output folder' % type)
	filename, file_extension = os.path.splitext(path)
	if type != file_extension[1:]:
		fu.log('Format %s in %s input file is not compatible' % (file_extension[1:], type), out_log)
		raise SystemExit('Format %s in %s input file is not compatible' % (file_extension[1:], type))

	return path

def get_output_path(path, out_log):
	""" Gets folder from output files """
	if not os.path.exists(os.path.dirname(path)):
		fu.log('Unexisting output file, exiting', out_log)
		raise SystemExit('Unexisting output folder')

	return os.path.dirname(path)

def get_binary_path(properties, type):
	""" Gets binary path """
	return properties.get(type, get_default_value(type))

def get_basename(basename, out_log):
	""" Checks if provided basename value is correct """
	bsn = str(basename)
	if basename == '':
		fu.log('No basename provided, default value %s assigned' % get_default_value('basename'), out_log)
		bsn = get_default_value('basename')

	return bsn

def get_charge(charge, out_log):
	""" Checks if provided charge value is correct """
	ch = charge
	if ch == '':
		fu.log('No charge provided, default value %s assigned' % get_default_value('charge'), out_log)
		ch = get_default_value('charge')

	if not isinstance(ch, int):
		fu.log('Value %s is not compatible as a charge value, default value %d assigned' % (ch, get_default_value('charge')), out_log)
		ch = get_default_value('charge')

	return str(ch)

def get_default_value(key):
	""" Gives default values according to the given key """
	default_values = {
		"charge": 0,
		"basename": "BBB",
		"acpype_path": "acpype",
		"AcpypeParamsGMX": {
			"topology": "GROMACS",
			"suffix": "_GMX."
		}
	}

	return default_values[key]

def is_valid_input(ext):
	""" Checks if input file format is compatible with Acpype """
	formats = ["pdb", "mdl", "mol2"]

	return ext in formats

def process_output(tmp_folder, files_folder, class_params, output_files, out_log):
	""" Moves and removes temporal files generated by the wrapper """
	path = os.path.join(tmp_folder, files_folder)
	suffix = class_params['suffix']
	src_files = glob.glob(path + '/*' + suffix + '*')
	# copy files for the requested topology to the output_path
	for file_name in src_files:
		if (os.path.isfile(file_name)):
			filename, file_extension = os.path.splitext(file_name)
			shutil.copy(file_name, output_files[file_extension[1:]])
			fu.log('File %s succesfully created' % output_files[file_extension[1:]], out_log)

	# remove temporary folder
	fu.rm(tmp_folder)
	fu.log('Removed temporary folder: %s' % tmp_folder, out_log)