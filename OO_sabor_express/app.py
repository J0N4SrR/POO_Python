from modelos.restaurante import Restaurante
from modelos.cardapio.bebidas import Bebida
from modelos.cardapio.prato import Prato



restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 5)
restaurante_mexicano = Restaurante('mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Saikai', 'Japonesa')

bebida_suco = Bebida ('Suco de Melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

restaurante_praca.exibir_cardapio()

def main():
    print(bebida_suco)
    print(prato_paozinho)



if __name__ == '__main__':
    main()