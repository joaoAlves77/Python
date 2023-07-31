# calculadore

def calculadora(operacao, num1, num2):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        return num1 / num2
    else:
        return "Operação invalida"

print(40* "=")
print("Boas vindas a calculadore python")
print(40* "=")

num1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))

resultado = calculadora(operacao, num1, num2)

print(f"{num1} {operacao} {num2} = {round(resultado,2)}")
