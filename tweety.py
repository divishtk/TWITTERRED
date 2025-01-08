from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data to serve
data = [
    {"id": 1, "name": "Alice", "role": "Engineer"},
    {"id": 2, "name": "Bob", "role": "Designer"},
    {"id": 3, "name": "Charlie", "role": "Manager"}
]

# Basic route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Simple Python GET API!"})

# GET all items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(data)

# GET item by ID
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item_by_id(item_id):
    item = next((item for item in data if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
