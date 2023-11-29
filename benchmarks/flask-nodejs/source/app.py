from flask import Flask, request, jsonify
from bcrypt import hashpw, gensalt
from db import read_items, write_items

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    # A simple endpoint that returns a greeting
    return "Hello World!"

@app.route('/grocery_items', methods=['GET'])
def get_grocery_items():
    # Endpoint to retrieve a list of grocery items
    try:
        # Fetching the grocery items from the database
        grocery_items = read_items()
        # Formatting the items for JSON response
        items = [{"id": item["id"], "name": item["name"], "price": item["price"]} for item in grocery_items]
        # Returning the items as a JSON response
        return jsonify(items)
    except Exception as e:
        # In case of an exception, return a 500 error
        return str(e), 500

@app.route('/grocery_items', methods=['POST'])
def add_grocery_item():
    # Endpoint to add a new grocery item
    try:
        # Retrieving the posted grocery item
        new_item = request.json
        # Logging for debugging purposes
        print(new_item["id"], new_item, flush=True)
        # Fetching the current list of grocery items from the database
        grocery_items = read_items()
        # Adding the new item to the list if it does not already exist
        if new_item not in grocery_items:
            grocery_items.append(new_item)
            # Writing the updated list back to the database
            write_items(grocery_items)
        # Returning a success response
        return "Successfully added item", 201
    except Exception as e:
        # In case of an exception, return a 500 error
        return str(e), 500
    
@app.route('/grocery_items/<int:item_id>', methods=['DELETE'])
def delete_grocery_item(item_id):
    # Endpoint to delete a grocery item by ID
    try:
        # Fetching the current list of grocery items from the database
        grocery_items = read_items()
        # Removing the item with the specified ID
        grocery_items = [item for item in grocery_items if item["id"] != item_id]
        # Writing the updated list back to the database
        write_items(grocery_items)
        # Returning a success response
        return "Successfully deleted item", 200
    except Exception as e:
        # In case of an exception, return a 500 error
        return str(e), 500

@app.route('/hashpassword/<string:password>', methods=['GET'])
def hash_password(password):
    # Endpoint to hash a password
    try:
        # Hashing the password using bcrypt
        hashed_password = hashpw(password.encode('utf-8'), gensalt())
        # Returning the hashed password in string format
        return hashed_password.decode('utf-8')
    except Exception as e:
        # In case of an exception, return a 500 error
        return str(e), 500

# Starting the Flask application if this file is the entry point to the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** Instead of returning bare exceptions (`return e, 500`), I've converted them to strings for consistent JSON response formatting (`return str(e), 500`). This change ensures the error messages are properly encoded and can be parsed by the client receiving the JSON response.