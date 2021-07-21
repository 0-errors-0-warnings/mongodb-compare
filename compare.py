#!/usr/bin/env python

import json
import os

def load_json_file(file_name):
    with open(file_name, 'r') as f:
        return json.load(f)


def to_key(key1, key2):
    return f'{key1}/{key2}'


def compare_items(item1, item2, key_path):
    #print(item1)
    #print(item2)
    for key, value in item1.items():
        if key not in item2.keys():
            print(f'key "{to_key(key_path, key)}" missing from target')
        else:
            if type(value) is dict:
                compare_items(value, item2[key], f'{to_key(key_path, key)}')
            elif value != item2[key]:
                print(f'value mismatch for key "{to_key(key_path, key)}". src: {value}, tgt: {item2[key]}')

    
item1 = load_json_file('data/1.json')
item2 = load_json_file('data/2.json')

print('src: 1.json, tgt: 2.json')
compare_items(item1, item2, '.')

print('\n\n')
print('src: 2.json, tgt: 1.json')
compare_items(item2, item1, '.')
