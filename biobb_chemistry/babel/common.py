""" Common functions for package biobb_chemistry.babel """
import os.path
import re
from biobb_common.tools import file_utils as fu


def check_input_path(path):
	""" Checks input file """ 
	if not os.path.exists(path):
		raise SystemExit('Unexisting input file')
	filename, file_extension = os.path.splitext(path)
	if not is_valid_input(file_extension[1:]):
		raise SystemExit('Format %s in input file is not compatible' % file_extension[1:])
	return path

def check_output_path(path):
	""" Checks output path and file """ 
	if not os.path.exists(os.path.dirname(path)):
		raise SystemExit('Unexisting output folder')
	filename, file_extension = os.path.splitext(path)
	if not is_valid_input(file_extension[1:]):
		raise SystemExit('Format %s in output file is not compatible' % file_extension[1:])
	return path

def check_input_path_minimize(path):
	""" Checks input file """ 
	if not os.path.exists(path):
		raise SystemExit('Unexisting input file')
	filename, file_extension = os.path.splitext(path)
	if not is_valid_input_minimize(file_extension[1:]):
		raise SystemExit('Format %s in input file is not compatible' % file_extension[1:])
	return path

def check_output_path_minimize(path):
	""" Checks output path and file """ 
	if not os.path.exists(os.path.dirname(path)):
		raise SystemExit('Unexisting output folder')
	filename, file_extension = os.path.splitext(path)
	if not is_valid_input_minimize(file_extension[1:]):
		raise SystemExit('Format %s in output file is not compatible' % file_extension[1:])
	return path

def get_parameters(properties, type):
	""" Gets configuration file parameters """
	if not properties.get(type, dict()):
		raise SystemExit('No ' + type + ' parameter provided')
	else:
		return properties.get(type, dict())

def get_binary_path(properties, type):
	""" Gets binary path """
	return properties.get(type, get_default_value(type))

def get_input_format(obj):
	""" Checks if provided input format is correct """
	out_log, err_log = fu.get_logs(path=obj.path, prefix=obj.prefix, step=obj.step, can_write_console=obj.can_write_console_log)

	infr = obj.input_format
	if not is_valid_input(infr):
		filename, file_extension = os.path.splitext(obj.input_path)
		fu.log('Format %s is not compatible as an input format, assigned input file extension: %s' % (infr, file_extension[1:]), out_log, obj.global_log)
		infr = file_extension[1:]

	return infr

def check_minimize_property(type, value, obj):
	""" Checks all minimize properties """
	out_log, err_log = fu.get_logs(path=obj.path, prefix=obj.prefix, step=obj.step, can_write_console=obj.can_write_console_log)
	value = str(value)

	if type == "criteria":
		if re.match('[+\-]?(?:0|[1-9]\d*)(?:\.\d*)?(?:[eE][+\-]?\d+)?', value):
			return True
		else:
			fu.log('Criteria %s is not correct, assigned default value: %s' % (value, get_default_value('criteria')), out_log, obj.global_log)

	if type == "method":
		if value in ['cg', 'sd']:
			return True
		else:
			fu.log('Method %s is not correct, assigned default value: %s' % (value, get_default_value('method')), out_log, obj.global_log)

	if type == "force_field":
		if value in ['GAFF', 'Ghemical', 'MMFF94', 'MMFF94s', 'UFF']:
			return True
		else:
			fu.log('Force field %s is not correct, no force field assigned' % (value), out_log, obj.global_log)

	if type == "hydrogens":
		if value == 'True':
			return True
		elif value == 'False':
			pass
		else:
			fu.log('Hydrogens %s is not correct, assigned default value: %s' % (value, get_default_value('hydrogens')), out_log, obj.global_log)

	if type == "steps":
		if re.match('^\d+$', value):
			return True
		else:
			fu.log('Steps %s is not correct, assigned default value: %s' % (value, get_default_value('steps')), out_log, obj.global_log)

	if type == "cutoff":
		if value == 'True':
			return True
		elif value == 'False':
			pass
		else:
			fu.log('Cut-off %s is not correct, assigned default value: %s' % (value, get_default_value('cutoff')), out_log, obj.global_log)

	if type == "rvdw":
		if re.match('(\d+(\.\d+)?)', value):
			return True
		else:
			fu.log('Rvdw %s is not correct, assigned default value: %s' % (value, get_default_value('rvdw')), out_log, obj.global_log)

	if type == "rele":
		if re.match('(\d+(\.\d+)?)', value):
			return True
		else:
			fu.log('Rele %s is not correct, assigned default value: %s' % (value, get_default_value('rele')), out_log, obj.global_log)

	if type == "frequency":
		if re.match('^\d+$', value):
			return True
		else:
			fu.log('Frequency %s is not correct, assigned default value: %s' % (value, get_default_value('frequency')), out_log, obj.global_log)

	return False


def get_output_format(obj):
	""" Checks if provided output format is correct """
	out_log, err_log = fu.get_logs(path=obj.path, prefix=obj.prefix, step=obj.step, can_write_console=obj.can_write_console_log)

	oufr = obj.output_format
	if not is_valid_output(oufr):
		filename, file_extension = os.path.splitext(obj.output_path)
		fu.log('Format %s is not compatible as an output format, assigned output file extension: %s' % (oufr, file_extension[1:]), out_log, obj.global_log)
		oufr = file_extension[1:]

	return oufr

def get_coordinates(obj):
	""" Checks if provided coordinates value is correct """
	out_log, err_log = fu.get_logs(path=obj.path, prefix=obj.prefix, step=obj.step, can_write_console=obj.can_write_console_log)

	crd = str(obj.coordinates)
	if crd != '3' and crd != '2':
		fu.log('Value %s is not compatible as a coordinates value' % crd, out_log, obj.global_log)
		crd = ''

	return crd


def get_default_value(key):
	""" Gives default values according to the given key """
	default_values = {
		"coordinates": 2,
		"obabel_path": "obabel",
		"obminimize_path": "obminimize",
		"criteria": 1e-6,
	  	"method": "cg",
	  	"hydrogens": False,
	  	"steps": 2500,
	  	"cutoff": False,
	  	"rvdw": 6.0,
	  	"rele": 10.0,
	  	"frequency": 10
	}

	return default_values[key]

def is_valid_input(ext):
	""" Checks if input file format is compatible with Open Babel """
	formats = ["abinit","acesout","acr","adfout","alc","aoforce","arc","axsf","bgf","box","bs","c09out","c3d2","caccrt","can","car","castep","ccc","cdjson","cdx","cdxml","cif","ck","cml","cmlr","CONFIG","CONTCAR","CONTFF","crk2d","crk3d","ct","cub","cube","dallog","dalmol","dat","dmol","dx","ent","exyz","fa","fasta","fch","fchk","fck","feat","fhiaims","fract","fs","fsa","g03","g09","g92","g94","g98","gal","gam","gamess","gamin","gamout","got","gpr","gro","gukin","gukout","gzmat","hin","HISTORY","inchi","inp","ins","jin","jout","log","lpmd","mcdl","mcif","MDFF","mdl","ml2","mmcif","mmd","mmod","mol","mol2","mold","molden","molf","moo","mop","mopcrt","mopin","mopout","mpc","mpo","mpqc","mrv","msi","nwo","orca","out","outmol","output","pc","pcjson","pcm","pdb","pdbqt","png","pos","POSCAR","POSFF","pqr","pqs","prep","pwscf","qcout","res","rsmi","rxn","sd","sdf","siesta","smi","smiles","smy","sy2","t41","tdd","text","therm","tmol","txt","txyz","unixyz","VASP","vmol","xml","xsf","xtc","xyz","yob"]
	return ext in formats

def is_valid_output(ext):
	""" Checks if output file format is compatible with Open Babel """
	formats = ["acesin","adf","alc","ascii","bgf","box","bs","c3d1","c3d2","cac","caccrt","cache","cacint","can","cdjson","cdxml","cht","cif","ck","cml","cmlr","com","confabreport","CONFIG","CONTCAR","CONTFF","copy","crk2d","crk3d","csr","cssr","ct","cub","cube","dalmol","dmol","dx","ent","exyz","fa","fasta","feat","fh","fhiaims","fix","fps","fpt","fract","fs","fsa","gamin","gau","gjc","gjf","gpr","gr96","gro","gukin","gukout","gzmat","hin","inchi","inchikey","inp","jin","k","lmpdat","lpmd","mcdl","mcif","MDFF","mdl","ml2","mmcif","mmd","mmod","mna","mol","mol2","mold","molden","molf","molreport","mop","mopcrt","mopin","mp","mpc","mpd","mpqcin","mrv","msms","nul","nw","orcainp","outmol","paint","pcjson","pcm","pdb","pdbqt","png","pointcloud","POSCAR","POSFF","pov","pqr","pqs","qcin","report","rsmi","rxn","sd","sdf","smi","smiles","stl","svg","sy2","tdd","text","therm","tmol","txt","txyz","unixyz","VASP","vmol","xed","xyz","yob","zin"]
	return ext in formats

def is_valid_input_minimize(ext):
	""" Checks if input file format is compatible with Obminimize """
	formats = ["pdb"]
	return ext in formats

def is_valid_output_minimize(ext):
	""" Checks if output file format is compatible with Obminimize """
	formats = ["pdb"]
	return ext in formats
