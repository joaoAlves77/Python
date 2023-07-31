# Operadores lógicos 

# AND - TODAS EXPRESSÕES VERDADEIRAS
# OR - PELO MENOS 1 EXPRESSÃO VERDADEIRA
# NOT - INVERTAR EXPRESSÃO

# exemplo and
sou = input("Escreva: ")
idade = int (input("Idade: "))

if(sou == "homem" and idade >= 18):
    print("Deve tirar")

# exemplo or 
estado = input("digite seu estado: ")

if(estado == "pernambuco" or estado == "bahia"):
    print("atende!")

 # exemplo not
doente = True
if(not doente):
    print("acesso liberado")