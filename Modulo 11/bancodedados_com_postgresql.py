
print("Hello, World!")

import sqlite3

# Conexão com o banco
con = sqlite3.connect("clientes.db")
cur = con.cursor()

# Criar tabela
cur.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

# Funções CRUD
def inserir():
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    cur.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", (nome, email))
    con.commit()
    print("Cliente inserido com sucesso!")

def consultar():
    cur.execute("SELECT * FROM Clientes")
    for row in cur.fetchall():
        print(row)

def atualizar():
    id = input("ID do cliente para atualizar: ")
    novo_nome = input("Novo nome: ")
    novo_email = input("Novo email: ")
    cur.execute("UPDATE Clientes SET nome=?, email=? WHERE id=?", (novo_nome, novo_email, id))
    con.commit()
    print("Cliente atualizado!")

def deletar():
    id = input("ID do cliente para deletar: ")
    cur.execute("DELETE FROM Clientes WHERE id=?", (id,))
    con.commit()
    print("Cliente deletado!")

def filtrar():
    cur.execute("SELECT * FROM Clientes WHERE nome LIKE 'A%'")
    for row in cur.fetchall():
        print(row)

# Menu simples
while True:
    print("\n1 - Inserir cliente")
    print("2 - Consultar clientes")
    print("3 - Atualizar cliente")
    print("4 - Deletar cliente")
    print("5 - Filtrar (nomes com A)")
    print("0 - Sair")

    opc = input("Escolha uma opção: ")

    if opc == "1":
        inserir()
    elif opc == "2":
        consultar()
    elif opc == "3":
        atualizar()
    elif opc == "4":
        deletar()
    elif opc == "5":
        filtrar()
    elif opc == "0":
        break
    else:
        print("Opção inválida!")

con.close()