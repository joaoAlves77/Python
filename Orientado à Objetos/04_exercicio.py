'''
Crie um programa que defina a classe "Carro"
com um construtor que receba dois parâmetros,
a cor e a marca do carro.
O programa deve criar duas instância da classe
"Carro", "c1" e "c2", com diferentes valores
para os parâmetros cor e marca.
Em seguida, o programa deve imprimir a cor e
a marca de cada um dos carros. 
'''
class Carro:
    def __init__(self, cor, marca):
        self.cor = cor
        self.marca = marca

c1 = Carro("Vermelho", "Fiat")
print(c1.cor)
print(c1.marca)

c2 = Carro("azul", "BMW")
print(c2.cor)
print(c2.marca)
