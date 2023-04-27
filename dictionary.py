from flask import request, jsonify

# Exemplo dicionário de produtos cadastrados
products = {
    1: {
    "id": 1,
    "name": "Fritadeira Elétrica sem Óleo/Air Fryer Philco",
    "description": "Fritadeira Elétrica sem Óleo/Air Fryer Philco - Gourmet PFR15PG Preto 3,2L com Timer",
    "brand": "Philco",
    "price": 392.64,
    "weight": 4.48
},
2: {
    "id": 2,
    "name": "Tanquinho Semiautomático Suggar 10Kg",
    "description": "Tanquinho Semiautomático Suggar 10Kg - Lavamax Eco",
    "brand": "Suggar",
    "price": 460.27,
    "weight": 10.19
},
3: {
    "id": 3,
    "name": "iPhone 11 Apple 64GB",
    "description": "iPhone 11 Apple 64GB Preto 6,1” 12MP iOS",
    "brand": "Apple",
    "price": 2825.10,
    "weight": 0.194
}
}

#create id
def create_id():
    id = max(products.keys()) + 1
    return id

# Return product
def return_product(id:int):
    if id in products.keys():
        return jsonify(products[id])
    else:
        return jsonify({"error": "Produto não encontrado"}), 404

# Return products
def return_products():
    return jsonify(products)

#create product
def create_product(id=None):
    if request.method == "POST":
        if id is None:
            id = create_id()
            while id in products:
                id = create_id()
            product = {
                'id': id,
                'name': request.json["name"],
                'description': request.json["description"],
                'brand': request.json["brand"],
                'price': request.json["price"],
                'weight': request.json["weight"]
            }
            products[id] = product
            return jsonify(products)        
    elif request.method == "PUT":
        id = request.json["id"]
        if id in products:
            product = products[id]
            product['name'] = request.json["name"]
            product['description'] = request.json["description"]
            product['brand'] = request.json["brand"]
            product['price'] = request.json["price"]
            product['weight'] = request.json["weight"]
            return jsonify(product), 200
        else:
            return jsonify({"error": "Produto não encontrado"}), 404

# Delete product
def delete_product(id:int):
    del products[id]
    return {}