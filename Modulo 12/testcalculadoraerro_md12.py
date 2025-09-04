import unittest

class Calculadora:
    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não permitida")
        return a / b

# programa principal com input
if __name__ == "__main__":
    calc = Calculadora()
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))

    try:
        print("Resultado da divisão:", calc.dividir(x, y))
    except ValueError as e:
        print("Erro:", e)

    unittest.main(exit=False)


class TestCalculadoraInvalidos(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)