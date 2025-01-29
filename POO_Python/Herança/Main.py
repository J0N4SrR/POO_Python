from Veiculos import Veiculos  
from Carro import Carro
from Moto import Moto

def main():
    v1 = Veiculos('Ford', 'Gol')
    v2 = Veiculos('Caminhão', 'Gl')
    v3 = Veiculos('R3', 'Sem ideia')
    c1 = Carro('Wolks', 'Uno', 4)
    c2 = Carro('Hiunday', 'HB20', 4)
    c3 = Carro('Ford', 'Celta', 2)
    m1 = Moto('Az', 'az21', 'Esportiva')
    m2 = Moto('Az', 'az223', 'Casual')
    m3 = Moto('Lamp', '2157', 'Casual')

    print(v1)
    print(v2)
    print(v3)
    print(c1)
    print(c2)
    print(c3)
    print(m1)
    print(m2)
    print(m3)

if __name__ == "__main__":
    main()
