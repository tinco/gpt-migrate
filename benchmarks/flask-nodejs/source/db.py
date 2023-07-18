import json

def read_items():
    """
    Read the grocery items from the 'storage/items.json' file.

    Returns:
        list: A list of grocery items loaded from the file.

    Raises:
        FileNotFoundError: If the 'storage/items.json' file does not exist.
        JSONDecodeError: If the contents of the file are not valid JSON.
    """
    with open('storage/items.json') as f:
        grocery_items = json.load(f)
    return grocery_items

def write_items(grocery_items):
    """
    Write the grocery_items to the 'storage/items.json' file.

    Args:
        grocery_items (list): A list of grocery items to be written.

    Raises:
        FileNotFoundError: If the 'storage/items.json' file does not exist.
    """
    with open('storage/items.json', 'w') as f:
        json.dump(grocery_items, f)
```
In the `read_items` function, we use the `open` function to open the 'storage/items.json' file in read mode. The grocery items are then loaded into the `grocery_items` variable using `json.load`. Finally, the function returns the `grocery_items` list.

In the `write_items` function, we use the `open` function to open the 'storage/items.json' file in write mode. The `grocery_items` list is then written to the file using `json.dump`.