from Veiculos import Veiculos  

class Carro(Veiculos):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = int(portas)

    def __str__(self):
            return super().__str__() + f' | Portas: {self.portas}'