#!/usr/bin/python3
"""Returns the dictionary description with simple data structure"""


import json

def class_to_json(obj):
    """Returns the dictionary description with simple data structure"""
    return obj.__dict__
