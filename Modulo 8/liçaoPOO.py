# 1 - Classe Carro
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

    def __str__(self):
        return f"{self.marca} {self.modelo}"


# 2 - Classe CarroEletrico herdando de Carro
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria

    def exibir_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, "
              f"Autonomia: {self.autonomia_bateria} km")

    def __str__(self):
        return f"{self.marca} {self.modelo} - Autonomia: {self.autonomia_bateria} km"


print("=== Meu Sistema de Carros ===")

# Criando carro comum
marca = input("Digite a marca do carro: ")
modelo = input("Digite o modelo do carro: ")
carro1 = Carro(marca, modelo)

# Criando carro elétrico
marca_e = input("Digite a marca do carro elétrico: ")
modelo_e = input("Digite o modelo do carro elétrico: ")
autonomia = int(input("Digite a autonomia da bateria (km): "))
carro2 = CarroEletrico(marca_e, modelo_e, autonomia)

print("\n--- Informações dos carros ---")
carro1.exibir_info()
carro2.exibir_info()

print("\n--- Usando __str__ ---")
print(carro1)
print(carro2)