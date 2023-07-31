'''
12 - Escreva um programa que leia uma string do usuário e
imprima a string invertida.
'''
frase = input("Digite um frase: ")
string_invertida = ''

for i in range(len(frase)-1,-1,-1):
    string_invertida += frase[i]
    
print(f"A string invertida é {string_invertida}")
'''
13 - Escreva um programa que leia uma string do usuário e
imprima a string em maiúsculas.
'''
frase = input("Digite uma frase: ")
strng_maiuscula = frase.upper()

print(f"A frase maiuscula é {strng_maiuscula}")
'''
14 - Escreva um programa que leia uma string do usuário e
imprima a string em minúsculas.
'''
frase = input("Digite uma frase: ")
strng_minuscula = frase.lower()

print(f"A frase minuscula é: {strng_minuscula}")
'''
15 - Escreva um programa que leia uma string do usuário e
imprima a string sem espaços.
'''
frase = input("Digite uma frase: ")
string_sem_espaco = frase.replace(" ", "")

print(f"A frase sem espaço fica {string_sem_espaco}")
'''
16 - Escreva um programa que leia duas strings do usuário e
verifique se são iguais.
'''
frase = input("Digite uma frase: ")
frase2 = input("Digite outra frase: ")
if frase == frase2:
    print("São iguais")
else:
    print("São diferentes")
'''
17 - Escreva um programa que leia uma string do usuário e
verifique se é um palíndromo (ou seja, que pode ser lida da
mesma forma de trás para frente).
'''
frase = input("Digite uma frase: ")
string_invertida = ""

for i in range(len(frase)-1, -1, -1):
    string_invertida += frase[i]

if frase == string_invertida:
    print("É uma palindromo")
else:
    print("Não é")
'''
18 - Escreva um programa que leia uma string do usuário e
imprima apenas as vogais da string.
'''
string = input("Digite uma string: ")

for caractere in string:
    if caractere in 'aeiouAEIOU':
        print(caractere, end ='')
'''
19 - Escreva um programa que leia uma string do usuário e
imprima apenas as consoantes da string.
'''
string = input("Digite uma string: ")

for caractere in string:
    if caractere.isalpha() and caractere not in 'aeiouAEIOU':
        print(caractere, end = '')
'''
20 - Escreva um programa que leia uma string do usuário e
imprima apenas os dígitos da string.
'''
string = input("Digite uma string: ")

for caractere in string:
    if caractere.isdigit():
        print(caractere, end = '')
'''
21 - Escreva um programa que leia uma string do usuário e
verifique se ela contém apenas dígitos.
'''
string = input("Digite uma string: ")
so_digitos = True

for caractere in string:
    if not caractere.isdigit():
        so_digitos = False
        break

if so_digitos == True:
    print("A string contem apenas digitos.")
else:
    print("a string não contem apenas digitos.")
'''
22 - Escreva um programa que leia uma string do usuário e
verifique se ela contém apenas letras.
'''
string = input("Digite uma string: ")
so_letras = True

for caractere in string:
    if not caractere.isdigit():
        so_letras = False
        break

if so_letras == True:
    print("A string contem apenas letras.")
else:
    print("A string não contem apenas letras. ")