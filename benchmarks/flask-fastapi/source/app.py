from flask import Flask, request, jsonify
from bcrypt import hashpw, gensalt
from db import read_items, write_items

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    """
    A route that returns a simple "Hello World!" message.

    Returns:
        str: The "Hello World!" message.
    """
    return "Hello World!"

@app.route('/grocery_items', methods=['GET'])
def get_grocery_items():
    """
    A route that retrieves grocery items.

    Returns:
        list: A list of dictionaries representing the grocery items. Each dictionary has the keys "id", "name", and "price".
    Raises:
        Exception: If there is an error retrieving the grocery items.
    """
    try:
        grocery_items = read_items()
        items = [{"id": item["id"], "name": item["name"], "price": item["price"]} for item in grocery_items]
        return jsonify(items)
    except Exception as e:
        return e, 500

@app.route('/grocery_items', methods=['POST'])
def add_grocery_item():
    """
    A route that adds a new grocery item.

    Returns:
        str: A success message indicating that the item was successfully added.
    Raises:
        Exception: If there is an error adding the grocery item.
    """
    try:
        new_item = request.json
        print(new_item["id"],new_item,flush=True)
        grocery_items = read_items()
        if new_item not in grocery_items:
            grocery_items.append(new_item)
            write_items(grocery_items)
        return "Successfully added item", 201
    except Exception as e:
        return e, 500
    
@app.route('/grocery_items/<int:item_id>', methods=['DELETE'])
def delete_grocery_item(item_id):
    """
    A route that deletes a grocery item.

    Args:
        item_id (int): The ID of the grocery item to delete.

    Returns:
        str: A success message indicating that the item was successfully deleted.
    Raises:
        Exception: If there is an error deleting the grocery item.
    """
    try:
        grocery_items = read_items()
        grocery_items = [item for item in grocery_items if item["id"] != item_id]
        write_items(grocery_items)
        return "Successfully deleted item", 200
    except Exception as e:
        return e, 500

@app.route('/hashpassword/<string:password>', methods=['GET'])
def hash_password(password):
    """
    A route that hashes a password using bcrypt.

    Args:
        password (str): The password to hash.

    Returns:
        str: The hashed password.
    Raises:
        Exception: If there is an error hashing the password.
    """
    try:
        return hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')
    except Exception as e:
        return e, 500

if __name__ == '__main__':
    app.run(debug=True)