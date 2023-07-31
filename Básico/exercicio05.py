'''
Faça um programa que receba a altura e o peso do usuario
e calcule o seu IMC utilizando a fórmula abaixo
'''
# IMC = peso / (altura*altura)

altura = float(input("Digite a altura do usuário: "))
peso = float(input("Digite a peso do usuário: "))

IMC = peso / (altura*altura)

print(f"O IMC é igual a {IMC:.2f}")
