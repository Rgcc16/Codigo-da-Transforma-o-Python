# Atividade 1 - Calculadora com tratamento de divisão por zero
try:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print("Resultado da divisão:", n1 / n2)
except ZeroDivisionError:
    print("Erro: divisão por zero!")
except ValueError:
    print("Erro: digite apenas números.")

# Atividade 2 - Conta bancária com exceção personalizada
class SaldoInsuficienteError(Exception):
    pass

saldo = 100
try:
    saque = float(input("\nDigite o valor do saque: "))
    if saque > saldo:
        raise SaldoInsuficienteError
    saldo -= saque
    print("Saque realizado! Saldo:", saldo)
except SaldoInsuficienteError:
    print("Erro: saldo insuficiente.")

# Atividade 3 - Validação de idade
try:
    idade = int(input("\nDigite sua idade: "))
    if idade <= 0:
        print("Erro: idade deve ser positiva.")
    else:
        print("Idade válida:", idade)
except ValueError:
    print("Erro: digite um número inteiro.")

# Desafio Extra - Login
usuario_correto = "admin"
senha_correta = "123"
tentativas = 3

while tentativas > 0:
    u = input("\nUsuário: ")
    s = input("Senha: ")
    if u == usuario_correto and s == senha_correta:
        print("Login bem-sucedido!")
        break
    else:
        tentativas -= 1
        print("Credenciais inválidas. Tentativas restantes:", tentativas)

