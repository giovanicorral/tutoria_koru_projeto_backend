from flask import Flask, request, jsonify
import repositorio

app = Flask(__name__)

#ROTA PARA RETORNAR TODOS OS PRODUTOS
@app.route("/products", methods=["GET"])
def get_products():
    lista_products = repositorio.retornar_produtos()
    return jsonify(lista_products)

#ROTA PARA RETORNAR UM PRODUTO
@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    product = repositorio.retornar_produto(id)

    if product:
        return jsonify(product)
    else:
        return jsonify({"message": "Produto não encontrado!"}), 404
    
#ROTA PARA CADASTRAR UM PRODUTO
@app.route("/products", methods=["POST"])
def criar_produtos():
    product = request.json
    id_product = repositorio.criar_produto(**product)
    product["id"] = id_product
    return jsonify(product), 201

#ROTA PARA ALTERAR UM PRODUTO
@app.route("/products/<int:id>", methods=["PUT"])
def atualizar_produto(id):
    product = repositorio.retornar_produto(id)
    if product:
        dados_atualizados = request.json
        dados_atualizados["id"] = id
        repositorio.atualizar_produto(**dados_atualizados)
        return(jsonify(dados_atualizados))
    else:
        return jsonify({"message": "Produto não encontrado"}), 404
    
#ROTA PARA DELETAR UM PRODUTO
@app.route("/products/<int:id>", methods=["DELETE"])
def remover_produto(id):
        product = repositorio.retornar_produto(id)
        if product:
            repositorio.remover_produto(id)
            return jsonify({"message":"Produto removido com sucesso"})
        else:
            return jsonify({"message":"Produto não encontrado"}), 404

app.run(debug=True)