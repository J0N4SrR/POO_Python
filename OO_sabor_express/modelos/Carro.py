class Carro:
    carros = []
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)
    
    def lista_carros():
        for carro in Carro.carros:
            print(f'{carro.modelo} | {carro.cor} | {carro.ano}')

c1 = Carro('Celta','azul',1990)
c2 = Carro('T-Cross', 'preta', 2025)

Carro.lista_carros()



