from flask import Flask, request, jsonify
import repositorio

app = Flask(__name__)

#ROTA PARA RETORNAR TODOS OS PRODUTOS
@app.route("/products", methods=["GET"])
def get_products(): 
    lista_products = repositorio.retornar_produtos() 
    return jsonify(lista_products)

#ROTA PARA RETORNAR UM ÚNICO PRODUTO
@app.route("/products/<int:id>", methods=["GET"])
def get_product(id): #Colocamos o 'id' para retornar um produto específico
    product = repositorio.retornar_produto(id)

    if product:
        return jsonify(product)
    else:
        return jsonify({"message": "Produto não encontrado!"}), 404 #Código de página que não existe
    
#ROTA PARA CADASTRAR UM PRODUTO
@app.route("/products", methods=["POST"])
def create_products():
    product = request.json #Vamos pegar exatamente o json enviado pela requisição
    id_product = repositorio.criar_produto(**product) #Utilizamos o '**product' pois vai receber exatamente as variaveis contidas em criar_produtos no nosso repositorio.py
    product["id"] = id_product #Incluindo o id criado no dicionario para que retorne, assim sabemos qual o id criado
    return jsonify(product), 201 #Código de sucesso na criação

#ROTA PARA ALTERAR UM PRODUTO
@app.route("/products/<int:id>", methods=["PUT"]) #Chamamos pelo id
def update_products(id):
    product = repositorio.retornar_produto(id) #Estamos verificando se o produto existe
    if product:
        dados_atualizados = request.json 
        dados_atualizados["id"] = id #Se tiver encontrato o produto acrescentamos o id pois já confirmamos que ele existe
        repositorio.atualizar_produto(**dados_atualizados)
        return(jsonify(dados_atualizados))
    else:
        return jsonify({"message": "Produto não encontrado"}), 404 #Código de página que não 
    
#ROTA PARA DELETAR UM PRODUTO
@app.route("/products/<int:id>", methods=["DELETE"]) #Chamamos pelo id
def delete_products(id):
        product = repositorio.retornar_produto(id)
        if product:
            repositorio.remover_produto(id) #Se encontrar o id o produto é excluído
            return jsonify({"message":"Produto removido com sucesso"})
        else:
            return jsonify({"message":"Produto não encontrado"}), 404 #Código de página que não 

app.run(debug=True)