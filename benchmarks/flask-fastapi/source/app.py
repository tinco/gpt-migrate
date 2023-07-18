"""
Module: app
Description: This module contains the Flask application for managing grocery items and hashing passwords.

Classes:
    None

Functions:
    hello_world() -> str
    get_grocery_items() -> Union[list[dict], Tuple[str, int]]
    add_grocery_item() -> Union[str, int]
    delete_grocery_item(item_id: int) -> Union[str, int]
    hash_password(password: str) -> Union[str, int]

Exceptions:
    None

Usage:
    - Start the Flask application by running this module directly.
    - Access the different routes of the application to manage grocery items and hash passwords.
"""

from flask import Flask, request, jsonify
from bcrypt import hashpw, gensalt
from db import read_items, write_items

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    """
    Returns a simple "Hello World!" message.

    Returns:
        str: A greeting message.
    """
    return "Hello World!"

@app.route('/grocery_items', methods=['GET'])
def get_grocery_items():
    """
    Fetches all the grocery items from the database.

    Returns:
        Union[list[dict], Tuple[str, int]]: If successful, returns a list of grocery items in JSON format.
            If an exception occurs, returns a tuple containing the error message and the HTTP status code.
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
    Adds a new grocery item to the database.

    Returns:
        Union[str, int]: If successful, returns a success message and the HTTP status code 201.
            If an exception occurs, returns the error message and the HTTP status code 500.
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
    Deletes a grocery item from the database.

    Args:
        item_id (int): The ID of the grocery item to be deleted.

    Returns:
        Union[str, int]: If successful, returns a success message and the HTTP status code 200.
            If an exception occurs, returns the error message and the HTTP status code 500.
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
    Hashes the provided password using bcrypt.

    Args:
        password (str): The password to be hashed.

    Returns:
        Union[str, int]: If successful, returns the hashed password as a string.
            If an exception occurs, returns the error message and the HTTP status code 500.
    """
    try:
        return hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')
    except Exception as e:
        return e, 500

if __name__ == '__main__':
    app.run(debug=True)