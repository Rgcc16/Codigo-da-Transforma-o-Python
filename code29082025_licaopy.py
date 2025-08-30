import random
import math
from datetime import datetime, date

# --- 1. Funções matemáticas ---
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def potencia(a, b):
    return a ** b


# --- 2. Funções com datas ---
def hoje():
    return date.today()


# --- 3. Jogo de adivinhação ---
def jogar():
    numero_secreto = random.randint(1, 100)
    tentativa = int(input("Adivinhe um número entre 1 e 100: "))

    diferenca = abs(numero_secreto - tentativa)

    if tentativa == numero_secreto:
        print("🎉 Parabéns! Você acertou!")
    else:
        print(f"❌ Você errou! O número era {numero_secreto}.")
        print("Diferença:", diferenca)
        print("Raiz quadrada da diferença:", math.sqrt(diferenca))


# --- Programa Principal ---
if __name__ == "__main__":
    # Testando funções matemáticas
    print("Soma:", soma(5, 3))
    print("Subtração:", subtracao(10, 4))
    print("Potência:", potencia(2, 3))

    print("-" * 30)

    # Testando datetime
    agora = datetime.now()
    print("Data e hora atuais:", agora)
    print("Data formatada:", agora.strftime("%d/%m/%Y"))
    print("Data de hoje (função hoje):", hoje())

    print("-" * 30)

    # Jogar
    jogar()

