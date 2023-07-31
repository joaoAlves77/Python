'''
Faça um programa que receba um número X digitado pelo usuário e 
imprima todos os números de X até 0 utilizando o while
'''
x = int(input("Digite um número: "))

while(x >= 0):
    print(x)
    x -= 1
'''
Faça um programa que imprima 7 vezes na tela
do usuário a frase: "Você consegue" utilizando
o laço de repeticão while
'''
i = 1
while(i <= 7):
    print("voce consegue")
    i += 1
'''
Faça um programa que imprima todos os números entre
100 e 1000 utilizando o while
'''
i = 100
while(i <= 1000):
    print(i)
    i += 1

'''
Faça um programa que inicie um laço de repetição que execute 
infinitamente.
Dentro do while, declare uma variavel chamada numero
que recebera uma entrada do usuario, o programa deve
continuar solocitando até que o numero digitado seja 0, ai
o laço será encerrado
'''
while(True):
    num = int(input("Digite um numero: "))
    if(num == 0):
        break
print("Fim")

'''
Faça um programa que declare uma variavel chamada continua
e execute um laço while, enquanto a variavel continua for ==
a "s", dentro do while, o usuario deve digitar um número e o 
programa deve imprimir dobro do número digitado.

E apos essa impressão, perguntar se o usuario deseja continuar
ou nao, se o usuario digitar 's', continua o laço, se o usuario 
digiatar 'n', então o laço acaba.. 
'''
continua = "s"
soma = 2
while(continua == "s"):
    num = int(input("Digite um número: "))
    soma *= num

    continua = input("Deseja continuar?(s/n): ")

print(f"Fim, total: {soma}")