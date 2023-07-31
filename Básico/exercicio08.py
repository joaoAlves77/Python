'''
Faça um programa que calcule o desconto de um produto
de acordo com a forma de pagamento escolhido pelo cliente

a vista 10%
cartão 5%
parcelado normal
'''
produto = int(input("Valor do produto: "))

print("1. vista 10%\n2. Cartão 5%\n3. Parcelado")
opcao = int(input("Escolha a forma de pagamento: "))

if(opcao == 1):
    calculo = produto * 0.90
    print(f"Preço final: {calculo}")
elif(opcao == 2):
    calculo = produto * 0.95
    print(f"Preço final: {calculo}")
elif(opcao == 3):
    print(f"Preço final: {produto}")
else:
    print("Invalido")
