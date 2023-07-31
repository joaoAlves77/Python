'''
Faça um programa que receba duas notas de 1 aluno 
e diga se ele foi aprovado ou não

Média acima 7 aprovado
abaixo, reprovado
'''

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite segunda nota: "))

media = (nota1+nota2)/2

if(media >= 7):
    print("Aprovado")
else:
    print("Reprovado")