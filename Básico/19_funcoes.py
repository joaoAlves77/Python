# funções part 1
# bloco de codigo que pode ser reutilizado no programa

def dizer_ola(nome):
    print(60*"*")
    print(f"Olá, bem vindo {nome}")
    print(60*"*")

nome = input("DIgite seu nome: ")
dizer_ola(nome)


# funções parte 2
# return - retorna um valor da função para o programa
def soma(num1, num2):
    return num1 + num2

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

minha_soma = soma(num1, num2)
print(minha_soma)


# Entendendo quando usar funções
def eh_par(num):
    if num % 2 == 0:
        print("par")
    else:
        print("impa")

numero = 10
eh_par(numero)


# Praticando um pouco mais funções

def eh_primo(num):
    # numero primo so tem 2 divisores!
    divisores = 0
    for i in range(1, num+1):
        if num % i == 0:
            divisores +=1

    if divisores == 2:
        return True
    else:
        return False
    
numero = int(input("Digite um numero: "))
print(eh_primo(numero))
