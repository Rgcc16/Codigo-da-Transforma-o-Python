from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# cria o banco e a tabela se não existir
def criar_banco():
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT
        )
    """)
    conexao.commit()
    conexao.close()

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()
    nome = dados.get("nome")
    email = dados.get("email")

    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()
    conexao.close()

    return jsonify({"mensagem": "Usuário salvo no banco de dados!"})

@app.route("/usuarios", methods=["GET"])
def listar():
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    lista = cursor.fetchall()
    conexao.close()

    return jsonify({"usuarios": lista})

if __name__ == "__main__":
    criar_banco()
    app.run(debug=True)