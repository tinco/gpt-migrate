import json

def read_items():
    """
    Reads the list of grocery items stored in the 'storage/items.json' file.
    
    Returns:
        grocery_items (list): The list of grocery items.
    """
    with open('storage/items.json') as f:
        grocery_items = json.load(f)
    return grocery_items

def write_items(grocery_items):
    """
    Writes the list of grocery items to the 'storage/items.json' file.
    
    Args:
        grocery_items (list): The list of grocery items.
    """
    with open('storage/items.json', 'w') as f:
        json.dump(grocery_items, f)