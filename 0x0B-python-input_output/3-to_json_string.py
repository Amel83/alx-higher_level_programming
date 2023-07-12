#!/usr/bin/python3
"""Defines a string-to-JSON func."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string."""
    return json.dumps(my_obj)
