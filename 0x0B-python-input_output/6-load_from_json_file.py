#!/usr/bin/python3
"""Deserializes a JSON object and writes it to a textfile"""

import json


def load_from_json_file(filename):
    """creates an Object from a 'JSON file'"""

    with open(filename, 'r') as f:
        json_data = f.read()
        return json.loads(json_data)
