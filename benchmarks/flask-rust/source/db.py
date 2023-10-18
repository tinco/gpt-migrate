import json

def read_items():
    """
    Reads the grocery items from the 'storage/items.json' file and returns them as a list.

    Returns:
        list: The grocery items loaded from the file.
    """
    with open('storage/items.json') as f:
        grocery_items = json.load(f)
    return grocery_items

def write_items(grocery_items):
    """
    Writes the given grocery items to the 'storage/items.json' file.

    Args:
        grocery_items (list): The list of grocery items to write to the file.
    """
    with open('storage/items.json', 'w') as f:
        json.dump(grocery_items, f)