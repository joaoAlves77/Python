# Laço de repetição While
while(True):
    print("Olá mundo")

# Laço de repetição while pt2
i = 1

while(i <= 200):
    print(i)
    i += 1

print("Olá")

# Laço de repetição while pt3
continua = "s"
soma = 0
while(continua == "s"):
    num = int(input("Digite um número: "))
    soma += num

    continua = input("Deseja contunar?(s/n): ")

print(f"FIm do programa, soma total: {soma}")