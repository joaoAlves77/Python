# Estrutura de repetição for
# For você sabe quantas vezes executar 
# While você não sabe quantas vezes executar
for i in range(2,10):
    print(i)


# For parte 2
frase = "Bora codar"

for caractere in frase:
    print(caractere)


# For parte 3
# Substituir vogais por *

frase = "Hello World"
nova_frase = ""
vogais = "aeiou"

for caractere in frase:
    if(caractere in vogais):
        nova_frase += "*"
    else:
        nova_frase += caractere

print(nova_frase)