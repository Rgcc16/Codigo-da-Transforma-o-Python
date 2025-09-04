from flask import Flask

app = Flask(__name__)

@app.route("/saudacao")
def saudacao():
    return {"mensagem": "Oi! Seja bem-vindo!"}

if __name__ == "__main__":
    app.run(debug=True)