'''
Faça um programa que receba a entrada do usuario em KM
e convertar para M, após isso, imprima na tela utilizando
o f-string
'''
km = float(input("Digite a entrada em KM: "))
m = km * 1000

print(f"A conversão de {km} KM é {m} metrôs")