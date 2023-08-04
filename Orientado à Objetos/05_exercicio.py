'''
Crie um programa que defina a classe "Circulo"
com um construtor que receba um parametro,
o raio do circulo.
O programa deve criar duas instancias da classe
"Circulo", "c1" e "c2", com diferentes valores 
para o parametro raio.
Em seguida, o programa deve imprimir o raio e
a area de cada um dos circulos criados.
'''

class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.area = raio*raio*3.14 

c1 = Circulo(3)
print(f"Raio: {c1.raio}\nArea: {c1.area}")

c2 = Circulo(2.90)
print(f"Raio: {c2.raio}\nArea: {c2.area}")