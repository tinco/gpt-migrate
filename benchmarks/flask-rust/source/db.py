"""
This module provides functions for reading and writing grocery items from/to a JSON file.

The `read_items` function reads the grocery items from the 'storage/items.json' file and returns them as a Python dictionary.

:param None:
:return: A dictionary of grocery items
:raises FileNotFoundError: If the 'storage/items.json' file is not found

The `write_items` function takes a dictionary of grocery items as input and writes them to the 'storage/items.json' file.

:param grocery_items: The dictionary of grocery items to be written
:return: None
:raises FileNotFoundError: If the 'storage/items.json' file is not found
"""

import json

def read_items():
    """
    Read grocery items from a JSON file and return them as a dictionary.

    :param None:
    :return: A dictionary of grocery items
    :raises FileNotFoundError: If the JSON file is not found
    """
    with open('storage/items.json') as f:
        grocery_items = json.load(f)
    return grocery_items

def write_items(grocery_items):
    """
    Write grocery items to a JSON file.

    :param grocery_items: The dictionary of grocery items to be written
    :return: None
    :raises FileNotFoundError: If the JSON file is not found
    """
    with open('storage/items.json', 'w') as f:
        json.dump(grocery_items, f)