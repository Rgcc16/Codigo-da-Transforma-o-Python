print("🌟 Minha Lista de Desejos para o Futuro 🌟\n") # Corrigido: Usado '\n' para nova linha e removida a divisão de string.

# Define o nome do arquivo onde os desejos serão salvos.
NOME_ARQUIVO = "meus_desejos.txt"
desejos = [] # Lista vazia para guardar desejos

# --- Carregar desejos existentes (se houver) ---
try:
    # 'r' significa modo de leitura (read)
    # 'with open'(...) as f:' garante que o arquivo seja fechado
    # automaticamente, mesmo que ocorra um erro.
    with open(NOME_ARQUIVO, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            #.strip() remove espaços em branco e quebras de linha indesejada.
            desejos.append(linha.strip())
    print(f"Meus desejos foram carregados do arquivo '{NOME_ARQUIVO}'!\n")
except FileNotFoundError:
    # Se o arquivo não existir, é a sua primeira vez que o programa está rodando.
    print(f"Parece que é sua primeira vez! Vamos criar sua Lista de desejos.\n")
except Exception as e:
    # Captura outros erros inesperados.
    print(f"Ocorreu um erro ao carregar os desejos: {e}")

# --- Função para salvar desejos no arquivo ---
def salvar_desejos(lista_de_desejos):
    try:
        # 'w' significa modo de escrita (write). Ele cria o arquivo se não existir
        # e apaga o conteúdo existente se ele já existir.
        # 'encoding="utf-8" ' é importante para caracteres especiais (acentos, emojis).
        with open(NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo:
            for desejo in lista_de_desejos:
                arquivo.write(desejo + '\n') # Escreve cada desejo seguido de uma nova linha.
        print("\n✅ Seus desejos foram salvos com sucesso!")
    except Exception as e:
        print(f"\n❌ Erro ao salvar os desejos: {e}")

# --- Loop Principal do Programa ---
while True:
    print("\n--- O que você quer fazer? ---")
    print("1 - Adicionar um novo desejo")
    print("2 - Ver meus desejos")
    print("3 - Sair")

    opcao = input("Digite sua opção (1, 2, ou 3): ")

    if opcao == "1":
        novo_desejo = input("Qual é o seu novo desejo para o futuro? ")
        if novo_desejo.strip(): # Verifica se o desejo não está vazio após remover espaços
            desejos.append(novo_desejo.strip()) # Adiciona o desejo à lista
            salvar_desejos(desejos) # Salva a lista toda vez que um desejo é adicionado
        else:
            print("Desejo não pode ser vazio! Tente novamente.")

    elif opcao == "2":
        print("\n✨ Seus Desejos para o Futuro ✨")
        if not desejos:
            print("Você ainda não tem desejos na sua lista. Que tal adicionar um?")
        else:
            for i, desejo in enumerate(desejos):
                print(f"{i+1}. {desejo}")
            print("------------------------------") # Adicionado para melhor formatação

    elif opcao == "3": # Corrigido: Adicionado '==' para comparação
        print("Até a próxima! Continue sonhando alto! �")
        break # Sai do loop, encerrando o programa

    else:
        print("Opção inválida. Por favor, digite 1, 2 ou 3.")