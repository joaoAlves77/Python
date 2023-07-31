# Projeto de conta bancária 
# Atributos: nome, saldo
# Metodos: Mostrar saldo, sacar, depositar

# Adicionar novas funções:
# 1. historico de deposito e saque
# 2. taxas para saque
# 3. limite o saque apos sacar o valor x
# 4. tranferencia entre contas!!!

class ContaBancaria:
    def __init__(self, nome_titular, saldo_inicial):
        self.nome_titular = nome_titular
        self.saldo = saldo_inicial
        self.saque_total = 0
        self.extrato = []

    def exebir_saldo(self):
        print(f"Saldo atual: {self.saldo}")

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito
        self.extrato.append("+ R$" + str(valor_deposito))
        print(f"Valor R$ {valor_deposito} foi depositado")
        self.exebir_saldo()

    def sacar(self, valor_saque):
        taxa = 5
        valor_taxa = valor_saque * (taxa/100)
        if valor_saque > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saque_total += valor_saque
            limite = 100 

            if(self.saque_total > limite):
                print("Limite atigido!")
            else:
                self.extrato.append("- R$" + str(valor_saque))
                self.saldo -= (valor_saque + valor_taxa)
                print(f"Valor R$ {valor_saque} foi retiradp da conta!")
                print(f"Taxa: R$ {valor_taxa}")
                self.exebir_saldo()
        
    def exibir_extrato(self):
        print("\nEXTRATO:")
        for item in self.extrato:
            print(item)
    def tranferir(self, valor_transf, conta_destino):
        self.saldo -= valor_transf
        conta_destino.depositar(valor_transf)
        print(f"Tranferencia de {valor_transf} realizada")
        self.extrato.append("- R$" + str(valor_transf))

conta1 = ContaBancaria("jose", 50)
conta1.depositar(50)
conta1.sacar(45)

conta2 = ContaBancaria("maria", 200)
conta2.tranferir(30, conta1)

conta1.exebir_saldo()
conta2.exebir_saldo()