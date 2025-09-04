import unittest

class Calculadora:
    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):
        return a / b

# programa principal com input
if __name__ == "__main__":
    calc = Calculadora()
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))

    print("Soma:", calc.somar(x, y))
    print("Divisão:", calc.dividir(x, y))

    unittest.main(exit=False)


class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_somar(self):
        self.assertEqual(self.calc.somar(2, 3), 5)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)