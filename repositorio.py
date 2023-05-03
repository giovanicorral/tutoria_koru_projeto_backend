from flask import Flask, jsonify, request, json
import sqlite3


#id generator
def gerar_id():
    conn = sqlite3.connect("produtos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT seq FROM sqlite_sequence WHERE name='produtos'")
    id = cursor.fetchone()[0]
    conn.close()
    return id + 1

#create
def criar_produto(name, description, brand, price, weight):
    try:
        conn = sqlite3.connect("produtos.db")
        cursor = conn.cursor()
        sql_insert = "INSERT INTO produtos (name, description, brand, price, weight) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(sql_insert, (name, description, brand, price, weight))
        product_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return product_id
    except Exception as ex:
        print(ex)
        return 0

#update
def atualizar_produto(id:int, name, description, brand, price, weight):
    try:
        conn = sqlite3.connect("produtos.db")
        cursor = conn.cursor()
        sql_update = "UPDATE produtos SET name = ?, description = ?, brand = ?, price = ?, weight = ? WHERE id = ?"
        cursor.execute(sql_update, (name, description, brand, price, weight, id))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False
    
#delete
def remover_produto(id:int):
    try:
        conn = sqlite3.connect("produtos.db")
        cursor = conn.cursor()
        sql_delete = "DELETE FROM produtos WHERE id = ?"
        cursor.execute(sql_delete, (id, ))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False

#read
def retornar_produto(id:int): 
    try:
        if id == 0:
            return gerar_id(), "", "", "", "", ""
        conn = sqlite3.connect("produtos.db")
        cursor = conn.cursor()
        sql_select = "SELECT * FROM produtos WHERE id = ?"
        cursor.execute(sql_select, (id, ))
        id, name, description, brand, price, weight = cursor.fetchone()
        
        conn.close()
        return { 
                "id":id, 
                "name":name, 
                "description":description, 
                "brand":brand, 
                "price":price, 
                "weight":weight
                }
    except Exception as ex:
        print(ex)
        return False

def retornar_produtos() -> list:
    try:       
        resultado = []
        conn = sqlite3.connect("produtos.db")
        cursor = conn.cursor()
        sql_select = "SELECT * FROM produtos"
        cursor.execute(sql_select)
        produtos = cursor.fetchall()
        conn.close()
        for item in produtos: #Para cada item em produto vou criar um objeto com o nome de produto que vai ser um dicionário
            produtos = {
                'id':item [0], #Cada valor em colchete é a posição na tabela
                'name':item [1],
                'description':item [2],
                'brand':item [3],
                'price':item [4],
                'weight':item [5]
            }
            resultado.append(produtos) #Percorremos cada resultado que veio e transformando em dicionário e colocamos na nossa lista 'resultado'
        
        conn.close()
        return resultado 
    except Exception as ex:
        print(ex)
        return False



