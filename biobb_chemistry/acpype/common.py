""" Common functions for package biobb_chemistry.acpype """
from pathlib import Path, PurePath
import glob
import shlex
import shutil
import string
import random
import fileinput
from biobb_common.tools import file_utils as fu


def check_input_path(path, out_log, classname):
    """ Checks input file """
    if not Path(path).exists():
        fu.log(classname + ': Unexisting input file, exiting', out_log)
        raise SystemExit(classname + ': Unexisting input file')
    file_extension = PurePath(path).suffix
    if not is_valid_input(file_extension[1:]):
        fu.log(classname + ': Format %s in input file is not compatible' % file_extension[1:], out_log)
        raise SystemExit(classname + ': Format %s in input file is not compatible' % file_extension[1:])
    if (PurePath(path).name == path or not PurePath(path).is_absolute()):
        path = str(PurePath(Path.cwd()).joinpath(path))

    return path


def check_output_path(path, type, out_log, classname):
    """ Checks output path """
    if PurePath(path).parent and not Path(PurePath(path).parent).exists():
        fu.log(classname + ': Unexisting output %s output folder, exiting' % type, out_log)
        raise SystemExit(classname + ': Unexisting %s output folder' % type)
    file_extension = PurePath(path).suffix
    if type != file_extension[1:]:
        fu.log(classname + ': Format %s in %s input file is not compatible' % (file_extension[1:], type), out_log)
        raise SystemExit(classname + ': Format %s in %s input file is not compatible' % (file_extension[1:], type))

    return path


# acpype options available as properties: property name -> (acpype flag, acpype default)
ACPYPE_OPTIONS = {
    "charge_method": ("-c", "bcc"),
    "multiplicity": ("-m", 1),
    "atom_type": ("-a", "gaff2"),
    "protein_ff": ("-F", "ff14SB"),
    "qprog": ("-q", "sqm"),
    "keyword": ("-k", None),
    "max_time": ("-s", 10800),
    "predindex": ("-r", 4),
    "gmx4": ("-z", False),
    "merge": ("-g", False),
    "sorted": ("-l", False),
    "cnstop": ("-t", False),
    "chiral": ("-j", False),
    "split_molecules": ("-S", False),
    "direct": ("-u", False),
}

# Accepted values of the options with a closed list of values
ACPYPE_CHOICES = {
    "charge_method": ["gas", "bcc", "abcg2", "user"],
    "atom_type": ["gaff", "amber", "gaff2", "amber2"],
    "protein_ff": ["ff14SB", "ff99SB"],
    "qprog": ["mopac", "sqm", "divcon"],
    "predindex": [0, 1, 2, 3, 4, 5],
}

# Options that acpype 2023.10.27 (the oldest supported version) does not have:
# they are only written to the command line when they are not the default value
ACPYPE_NEW_OPTIONS = {"protein_ff", "predindex", "split_molecules"}

# Options of the blocks that parameterize a molecule (-i input)
PARAMS_OPTIONS = ["charge_method", "multiplicity", "atom_type", "protein_ff", "qprog", "keyword", "max_time", "predindex"]
# Options of the GROMACS topologies
GMX_OPTIONS = ["gmx4", "merge", "sorted"]
# Options of the CNS topologies
CNS_OPTIONS = ["cnstop", "chiral"]
# Options of the AMBER to GROMACS conversion (-x inpcrd -p prmtop)
AMB2GMX_OPTIONS = GMX_OPTIONS + ["split_molecules", "direct"]


def get_acpype_options(obj, properties, names):
    """ Sets the given acpype options as attributes of the block, with the acpype default
    when they are not in the properties, so that the provenance records the values used """
    for name in names:
        setattr(obj, name, properties.get(name, ACPYPE_OPTIONS[name][1]))


def get_acpype_options_cmd(obj, names, out_log, classname):
    """ Returns the command line flags of the given acpype options of the block """
    instructions_list = []
    for name in names:
        flag, default = ACPYPE_OPTIONS[name]
        value = getattr(obj, name)
        if name in ACPYPE_CHOICES and value not in ACPYPE_CHOICES[name]:
            fu.log(classname + ': Value %s of the %s property is not valid, accepted values: %s' % (value, name, ', '.join(map(str, ACPYPE_CHOICES[name]))), out_log)
            raise SystemExit(classname + ': Value %s of the %s property is not valid' % (value, name))
        if isinstance(default, bool):
            if value:
                instructions_list.append(flag)
        elif value is None or value == '':
            continue
        elif name in ACPYPE_NEW_OPTIONS and value == default:
            continue
        elif name == "keyword":
            instructions_list.append(flag + ' ' + shlex.quote(str(value)))
        else:
            instructions_list.append(flag + ' ' + str(value))
    return instructions_list


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
    if ch is None or ch == '':
        fu.log('Charge will be guessed by acpype.', out_log)
        return ch

    if not isinstance(ch, (int, None)):  # type: ignore
        fu.log('Value %s is not compatible as a charge value, default value %d assigned' % (ch, get_default_value('charge')), out_log)
        ch = get_default_value('charge')

    return str(ch)


def create_unique_name(length=10, char=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(char) for x in range(length))


def get_default_value(key):
    """ Gives default values according to the given key """
    default_values = {
        "charge": 0,
        "basename": "BBB",
        "binary_path": "acpype",
        "AcpypeParamsGMX": {
            "topology": "GROMACS",
            "suffix": "_GMX."
        },
        "AcpypeParamsAC": {
            "topology": "Antechamber",
            "suffix": "_AC."
        },
        "AcpypeParamsGMXOPLS": {
            "topology": "OPLS/AA",
            "suffix": "_GMX_OPLS."
        },
        "AcpypeParamsCNS": {
            "topology": "GROMACS",
            "suffix": "_CNS."
        },
        "AcpypeConvertAMBERtoGMX": {
            "topology": "GMX",
            "suffix": "_GMX"
        }
    }

    return default_values[key]


def is_valid_input(ext):
    """ Checks if input file format is compatible with Acpype """
    formats = ["pdb", "mdl", "mol2"]

    return ext in formats


def process_output(unique_name, files_folder, basename, class_params, output_files, out_log):
    """ Moves and removes temporal files generated by the wrapper """
    path = files_folder
    suffix = class_params['suffix']
    src_files = glob.glob(path + '/' + basename + '.' + unique_name + suffix + '*')

    # copy files for the requested topology to the output_path
    for file_name in src_files:
        # replace random name by original name in all files
        with fileinput.FileInput(file_name, inplace=True) as file:
            for line in file:
                print(line.replace(basename + '.' + unique_name, basename), end='')

        if (Path(file_name).is_file()):
            file_extension = PurePath(file_name).suffix
            shutil.copy(file_name, output_files[file_extension[1:]])
            fu.log('File %s succesfully created' % output_files[file_extension[1:]], out_log)

    # if remove_tmp:
    #     # remove temporary folder
    #     fu.rm(files_folder)
    #     fu.log('Removed temporary folder: %s' % files_folder, out_log)


def process_output_gmx(unique_name, files_folder, basename, class_params, output_files, out_log):
    """ Moves and removes temporal files generated by the wrapper """
    path = files_folder
    suffix = class_params['suffix']
    src_files = glob.glob(path + '/' + basename + '.' + unique_name + suffix + '*')

    # copy files for the requested topology to the output_path
    for file_name in src_files:
        # replace random name by original name in all files
        with fileinput.FileInput(file_name, inplace=True) as file:
            for line in file:
                print(line.replace(basename + '.' + unique_name, basename), end='')

        if (Path(file_name).is_file()):
            file_extension = PurePath(file_name).suffix
            # in top files for gromacs, replace file.itp by name given by user
            if (file_extension[1:] == 'top') and ('itp' in output_files):
                with open(file_name) as f:
                    newText = f.read().replace(basename + '_GMX.itp', PurePath(output_files['itp']).name)
                with open(file_name, "w") as f:
                    f.write(newText)
            shutil.copy(file_name, output_files[file_extension[1:]])
            fu.log('File %s succesfully created' % output_files[file_extension[1:]], out_log)


def process_output_cns(unique_name, files_folder, basename, class_params, output_files, out_log):
    """ Moves and removes temporal files generated by the wrapper """
    path = files_folder
    suffix = class_params['suffix']
    src_files = glob.glob(path + '/' + basename + '.' + unique_name + suffix + '*')

    # copy files for the requested topology to the output_path
    for file_name in src_files:
        # replace random name by original name in all files
        with fileinput.FileInput(file_name, inplace=True) as file:
            for line in file:
                print(line.replace(basename + '.' + unique_name, basename), end='')

        if (Path(file_name).is_file()):
            file_extension = PurePath(file_name).suffix
            fu.log('Files: %s' % str(file_name), out_log)
            shutil.copy(file_name, output_files[file_extension[1:]])
            fu.log('File %s succesfully created' % output_files[file_extension[1:]], out_log)

    file_extension = ".pdb"
    file_name = path + '/' + basename + '.' + unique_name + "_NEW.pdb"
    with open(file_name) as f:
        newText = f.read().replace(basename + '_NEW.pdb', PurePath(output_files['pdb']).name)
    with open(file_name, "w") as f:
        f.write(newText)
    shutil.copy(file_name, output_files[file_extension[1:]])
    fu.log('File %s succesfully created' % output_files[file_extension[1:]], out_log)

    # if remove_tmp:
    #     # remove temporary folder
    #     fu.rm(files_folder)
    #     fu.log('Removed temporary folder: %s' % files_folder, out_log)
