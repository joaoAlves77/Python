'''
Faça um programa que receba a idade do usuário e diga se 
ele já pode tirar a habilitação ou não!
'''
idade = int(input("Digite sua idade: "))

if(idade >= 18):
    print("Você já pode tirar a habilitação")
else:
    print("Não pode tirar habilitação!")