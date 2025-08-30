# acesso
import json
import csv

# 1 - Criar e ler arquivo .txt
with open("informacoes.txt", "w") as arquivo_txt:
    arquivo_txt.write("Olá! Este é um teste de gravação em um arquivo .txt.\n")
    arquivo_txt.write("Segunda linha de informações.")

with open("informacoes.txt", "r") as arquivo_txt:
    conteudo_txt = arquivo_txt.read()
print("Conteúdo do TXT:")
print(conteudo_txt)

# 2 - Salvar e carregar dicionário em JSON
clientes = {
    "cliente1": {"nome": "Ana", "idade": 28, "email": "ana@email.com"},
    "cliente2": {"nome": "Carlos", "idade": 35, "email": "carlos@email.com"}
}

with open("clientes.json", "w") as arquivo_json:
    json.dump(clientes, arquivo_json, indent=4)

with open("clientes.json", "r") as arquivo_json:
    dados_json = json.load(arquivo_json)
print("\nConteúdo do JSON:")
print(dados_json)

# 3 - Criar e ler notas em CSV
notas = [
    ["Nome", "Nota"],
    ["Maria", 9.0],
    ["João", 7.5],
    ["Pedro", 8.2]
]

with open("notas.csv", "w", newline="") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(notas)

print("\nConteúdo do CSV:")
with open("notas.csv", "r") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        print(linha)
