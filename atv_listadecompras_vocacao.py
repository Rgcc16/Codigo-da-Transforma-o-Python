print("--- Lista de Compras ---")

NOME_ARQUIVO = "minha_lista.txt"
itens = []

# --- Carregar itens existentes ---
try:
    with open(NOME_ARQUIVO, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            itens.append(linha.strip())
    print(f"\nSeus itens foram carregados do arquivo '{NOME_ARQUIVO}'!\n")
except FileNotFoundError:
    print("\nParece que é sua primeira vez! Vamos criar sua Lista de Compras.\n")
except Exception as e:
    print(f"Ocorreu um erro ao carregar os itens: {e}")

# --- Função para salvar a lista ---
def salvar_itens(lista):
    try:
        with open(NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo:
            for item in lista:
                arquivo.write(item + '\n')
        print("\n✅ Lista salva com sucesso!")
    except Exception as e:
        print(f"\n❌ Erro ao salvar a lista: {e}")

# --- Menu principal ---
while True:
    print("\n--- Menu ---")
    print("1 - Adicionar item")
    print("2 - Ver lista")
    print("3 - Remover item")
    print("4 - Sair")

    opcao = input("Escolha uma opção (1 a 4): ")

    if opcao == "1":
        novo = input("Digite o novo item: ")
        if novo.strip():
            itens.append(novo.strip())
            salvar_itens(itens)
        else:
            print("Item não pode ser vazio!")

    elif opcao == "2":
        print("\n🛒 Sua Lista de Compras:")
        if not itens:
            print("A lista está vazia!")
        else:
            for i, item in enumerate(itens):
                print(f"{i+1}. {item}")
        print("-----------------------------")

    elif opcao == "3":
        if not itens:
            print("A lista está vazia, nada para remover.")
        else:
            print("\nItens na lista:")
            for i, item in enumerate(itens):
                print(f"{i+1}. {item}")
            try:
                num = int(input("Número do item que deseja remover: "))
                if 1 <= num <= len(itens):
                    removido = itens.pop(num - 1)
                    salvar_itens(itens)
                    print(f"'{removido}' foi removido!")
                else:
                    print("Número inválido.")
            except ValueError:
                print("Digite um número válido.")

    elif opcao == "4":
        print("Saindo... Até a próxima! 👋")
        break

    else:
        print("Opção inválida. Tente novamente.")
