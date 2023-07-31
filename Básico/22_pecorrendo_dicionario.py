'''
membros = ["sergio", "refem", "kodak"]
print(membros[1])

# Listas parte 2

frutas = ["goiaba", "maracuja", "maça"]
precos = [0.50, 0.78, 0.90]
quantidades = [10, 50, 90]

for i in range(3):
    print(f"{frutas[i]} custa {precos[i]} reias e possui {quantidades[i]}")
'''

frutas = {
    "goiaba":{"preco":0.50, "quantidade":10},
    "maracuja":{"preco":0.50, "quantidade":10},
    "maça":{"preco":0.50, "quantidade":10}
    }

for chave, valor in frutas.items():
    print(f"{chave} custa {valor['preco']} possui {valor['quantidade']}")