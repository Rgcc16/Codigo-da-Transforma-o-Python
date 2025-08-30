# Programa para separar números pares e ímpares com validação e salvamento

print("🔢 Classificador de Números: Pares e Ímpares\n")

# Listas principais
numeros = []   # Armazena todos os números digitados
pares = []     # Armazena números pares
impares = []   # Armazena números ímpares

# Arquivo para salvar os resultados
ARQUIVO = "numeros_classificados.txt"

# Pergunta quantos números o usuário quer digitar
while True:
    try:
        qtd = int(input("Quantos números você quer digitar? "))
        if qtd <= 0:
            print("Digite um número maior que zero.")
        else:
            break
    except ValueError:
        print("Digite apenas números inteiros.")

# Coleta dos números com validação
for i in range(qtd):
    while True:
        try:
            num = int(input(f"Digite o número {i+1}: "))
            numeros.append(num)
            break
        except ValueError:
            print("⚠️ Entrada inválida! Digite um número inteiro.")

# Classificando os números
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Exibindo resultado no terminal
print("\n✅ Classificação Final:")
print(f"🔵 Números Pares: {pares}")
print(f"🔴 Números Ímpares: {impares}")

# Salvando os dados em um arquivo
try:
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        arquivo.write("🔵 Números Pares:\n")
        for p in pares:
            arquivo.write(f"{p}\n")
        arquivo.write("\n🔴 Números Ímpares:\n")
        for i in impares:
            arquivo.write(f"{i}\n")
    print(f"\n📂 Resultados salvos no arquivo: {ARQUIVO}")
except Exception as e:
    print(f"❌ Erro ao salvar no arquivo: {e}")
