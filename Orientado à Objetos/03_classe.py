# Contrutor
# Inicializando os nosso atributos 

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("João", 21)
print(p1.nome)
print(p1.idade)

p2 = Pessoa("maria", 19)
print(p2.nome)
print(p2.idade)
