import json

def read_items():
    """Reads the grocery items from the JSON file.

    Returns:
        list: A list of grocery items.
    """
    with open('storage/items.json') as f:
        grocery_items = json.load(f)
    return grocery_items

def write_items(grocery_items):
    """Writes the grocery items to the JSON file.

    Args:
        grocery_items (list): A list of grocery items to be written.
    """
    with open('storage/items.json', 'w') as f:
        json.dump(grocery_items, f)
```

In the given code, the `read_items` function reads the grocery items from the `items.json` file located in the `storage` directory. It returns a list of grocery items.

The `write_items` function writes the provided `grocery_items` list to the `items.json` file. It overwrites the existing contents of the file with the new list.

Please note that the paths to the JSON file in both functions are relative to the root of the codebase, as specified in the given context.