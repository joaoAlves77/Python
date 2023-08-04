# Metodos de uma classe e self
class Carro:
    cor = "vermelho"

    def ligar(self):
        print("ligando o carro...")

carro1 = Carro()
print(carro1.cor)
carro1.ligar()
