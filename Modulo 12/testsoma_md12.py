import unittest

def soma(a, b):
    return a + b

# programa principal com input
if __name__ == "__main__":
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    print("Resultado da soma:", soma(x, y))

    unittest.main(exit=False)  # roda os testes depois da execução


class TestSoma(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(0, 0), 0)