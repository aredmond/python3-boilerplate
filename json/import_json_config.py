#!/usr/local/bin/python3
import json
from pprint import pprint
from os.path import dirname, realpath

# Find the file path of this script, not relative to where the scirp is excuting from
dir_path = dirname(realpath(__file__))
kittycat_json_file = dir_path + '/json_samples/awsstuff.json'

def import_json(jsonfile):
    with open(jsonfile) as data_file:
        data = json.load(data_file)
    return data

kittycat_config = import_json(kittycat_json_file)


for region, data in kittycat_config['Region'].items():
    print("*" + region + ("*"*40))
    print("  " + data['kittycatsg'])
    for vpc_info in data['vpcs']:
        print(vpc_info['vpcid'] + ': ' + vpc_info['vpcname'])
    print("*"*40)
