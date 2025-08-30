NOME_ARQUIVOmagico = "itens_magicos.txt"
itens = []

try:
    with open(NOME_ARQUIVOmagico, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            itens.append(linha.strip())
    print(f"\nSeus itens foram carregados do arquivo '{NOME_ARQUIVOmagico}'!\n")
except FileNotFoundError:
    print("\nParece que é sua primeira vez! Vamos entrar no mundo magico.\n")
except Exception as e:
    print(f"Ocorreu um erro ao carregar os itens: {e}")
    

def main():
    print(" --- Olá Mago ! --- ")
    while True:
        print(" --- Você é um grande mago ? --- ")
        print("1 --- Não sou ---")
        print("2 --- Sim sou --- ")

        opcao = input("\nDigite sua opção (1, 2, ou 3): ")

        if opcao == "1":
            print("\n- Então vá embora, trouxa! 🧹💨 -")
            break  

        elif opcao == "2":
            print("\n- Então venha conhecer meu mundo mágico! ✨🧙‍♂️ -")

            while True:
                print("\n--- Menu Mágico ---")
                print("1 - Descobrir item mágico -")
                print("2 - Ver todos os itens mágicos descorbertos - ")
                print("3 - Sair do mundo mágico -")

                opcao2 = input("\nDigite sua opção (1, 2, ou 3): ")
                
                if opcao2 == "1":
                    while True:
                        print ("\n--- Descobrir item mágico ---")
                        item_magico = input ("\nDigite o nome do item mágico que você deseja descobrir: ")
                        
                        if item_magico in ["Calise de Fogo", "Espelho de Ojesed", "Capa da Invisibilidade"]:
                            if item_magico not in itens:
                                itens.append(item_magico)
                                print(f"\nVocê descobriu o item mágico '{item_magico}'")
                            else:
                                print(f"\nVocê já descobriu o item mágico '{item_magico}' antes.")
                            while True:
                                print(" - Voce deseja continuar descobrindo itens mágicos ? - ")
                                print("1 - Sim - ")
                                print("2 - Não - ")

                                opcao3 = input("\nDigite sua opção (1 ou 2): ")

                                if opcao3 == "1":
                                    break  

                                if opcao3 == "2":
                                    print ("\n- Então vá embora -")
                                    return  
                        else:
                            print("Item mágico desconhecido, tente outro.")
                elif opcao2 == "2":
                    print("\nItens mágicos descobertos:")
                    for item in itens:
                        print("-", item)
                elif opcao2 == "3":
                    print("\nSaindo do mundo mágico...")
                    return  
                else:
                    print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
