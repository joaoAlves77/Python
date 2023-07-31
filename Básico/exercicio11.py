'''
Faça um programa que receba um numero X digitado pelo usuario
e imprima todos os numeros de 0 até X utilizando o for
'''
x = int(input("Digite um número: "))

for x in range(0, x):
    print(x)

'''
Faça um programa que imprima todos os números entre 
100 e 1000 utililizando o for 
'''
for i in range(100,1001):
    print(i)

'''
Faça um programa que imprima 10 vezes a frase:
For é facil, utilizando o for
'''
for i in range(11):
    print("Você consegue")

'''
Faça um programa que solicite um numero ao
usuario 10 vezes utilizando o for. E ao final do
programa, fora do for, imprima a soma de todos eles;
'''
soma = 0

for i in range(10):
    numero = float(input("Digite um número: "))
    soma += numero

print(f"A soma de todos os números é: {soma}")

'''
Faça um programa que imprima apenas os numeros 
pares de 2 ate 20 (dica: use 3 parametros)
'''
for i in range(2,21,2):
    print(i)

'''
Faça um programa que imprima os numeros de 20
ate 0, utilizando o for(dica: use 3 parâmetros e
o terceiro sera o numero -1)
'''
for i in range(20, -1, -1):
    print(i)
'''
Faça um programa que imprima a tabuada de 3 na
tela utilizando o for;
'''
for i in range(0, 31, 3):
    print(i)