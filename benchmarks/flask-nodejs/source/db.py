import json

def read_items():
    """
    Reads the grocery items from the 'storage/items.json' file and returns them as a list.
    
    Returns:
        list: A list of grocery items read from the file.
    """
    with open('storage/items.json') as f:
        grocery_items = json.load(f)
    return grocery_items

def write_items(grocery_items):
    """
    Writes the given grocery items to the 'storage/items.json' file.
    
    Args:
        grocery_items (list): A list of grocery items to be written to the file.
    """
    with open('storage/items.json', 'w') as f:
        json.dump(grocery_items, f)
```

In the given code, the `read_items()` function reads grocery items from the `storage/items.json` file and returns them as a list. The `write_items(grocery_items)` function writes the given grocery items to the `storage/items.json` file. The functions utilize the `json` module to handle the JSON data.