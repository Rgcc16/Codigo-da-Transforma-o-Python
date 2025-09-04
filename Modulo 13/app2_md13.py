from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []  # lista simples para guardar os usuários

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    dados = request.get_json()  # pega os dados enviados em JSON
    usuarios.append(dados)      # guarda na lista
    return jsonify({"mensagem": "Usuário cadastrado!", "usuarios": usuarios})

if __name__ == "__main__":
    app.run(debug=True)