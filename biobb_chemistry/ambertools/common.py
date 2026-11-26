""" Common functions for package biobb_chemistry.ambertools """


def get_binary_path(properties, type):
    """ Gets binary path """
    return properties.get(type, get_default_value(type))


def get_default_value(key):
    """ Gives default values according to the given key """
    default_values = {
        "binary_path": "reduce",
    }

    return default_values[key]
