'''
1 - Escreva um programa que imprima "Hello World" na tela.
'''
print("Hello word")
'''
2 - Escreva um programa que leia um número inteiro do
usuário e o imprima na tela.
'''
num = int(input("Digite um número: "))
print(num)
'''
3 - Escreva um programa que leia dois números inteiros do
usuário e imprima a soma deles.
'''
num = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
soma = num + num2
print(soma)
'''
4 - Escreva um programa que leia um número inteiro do
usuário e imprima se ele é par ou ímpar.
'''
num = int(input("Digite um número:"))
if(num % 2 == 0):
    print(f"numero: {num} é par.")
else:
    print(f"numero: {num} é impa.")
'''
5 - Escreva um programa que leia um número inteiro do
usuário e imprima se ele é positivo, negativo ou zero.
'''
num = int(input("Digite um numero: "))
if(num > 0):
    print("Positivo")
elif(num < 0):
    print("negativo")
else:
    ("zero")
'''
6 - Escreva um programa que leia uma temperatura em graus
Celsius e a converta em graus Fahrenheit. A fórmula de
conversão é F = (C * 1.8) + 32.
'''
c = float(input("Digite a temperatura: "))
f = (c * 1.8) + 32
print(f)
'''
7 - Escreva um programa que leia um número inteiro do
usuário e imprima seu fatorial.
'''
num = int(input("digite um numero: "))
fatorial = 1
for i in range(1, num, + 1):
    fatorial *= i
    print(f"O fatorial de {num} é {fatorial}")
'''
8 - Escreva um programa que leia um número inteiro do
usuário e imprima se ele é primo.
'''
num = int(input("digite um numero: "))
qtd_divisores = 0

if(num <= 1):
    qtd_divisores = 1
else:
    for i in range(2, num):
        if num % i == 0:
            qtd_divisores += 1

if(qtd_divisores == 2):
    print(f"O numero {num} é primo")
else:
    print(f"O numero {num} não é primo")
'''
9 - Escreva um programa que leia um número inteiro do
usuário e imprima todos os seus divisores.
'''
num = int(input("digite um numero: "))
for i in range(1, num):
    if num % i == 0:
        print(f"{i} é um divisor de {num}")
'''
10 - Escreva um programa que leia um número inteiro do
usuário e imprima sua tabuada.
'''
num = int(input("digite um numero: "))
for i in range(1,10):
    print(f"{num} x {i} = {num * i}")
'''
11 - Escreva um programa que leia uma string do usuário e
imprima o número de caracteres na string.
'''
str = input("digite uma string: ")
str_inverida = ""
for i in range(len(str)-1, -1, -1):
    str_inverida += str[i]
    print(str_inverida)
