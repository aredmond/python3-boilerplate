#!/usr/bin/python3
import yaml
from pprint import pprint
from os.path import dirname, realpath

dir_path = dirname(realpath(__file__))
tree_yaml_file = dir_path + '/tree.yml'

def import_yaml(yamlfile):
    with open(yamlfile) as data_file:
        data = yaml.safe_load(data_file)
    return data

yaml_data = import_yaml(tree_yaml_file)
pprint(yaml_data)
