from flask import Flask, request, jsonify
import dictionary

app = Flask(__name__)

# Route to return a single product by id
@app.route("/products/<int:id>", methods = ['GET'])
def show_product(id:int):
    return dictionary.return_product(id)

# Route to return all products
@app.route("/products", methods = ['GET'])
def show_all():
    return dictionary.return_products()

# Route to register a new product
@app.route("/products", methods = ['POST'])
def new_product():
    return dictionary.create_product()

# Route to update product
@app.route("/products/<int:id>", methods = ['PUT'])
def update_product(id):
    return dictionary.create_product(id)

# Route to delete product
@app.route("/products/<int:id>", methods = ['DELETE'])
def remove_product(id):
    return dictionary.delete_product(id)

app.run(debug=True)