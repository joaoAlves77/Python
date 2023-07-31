# Tratamento de exceções

try:
    num = int(input("Digite um numero: "))
    print(num)
except:
    print("Numero deve ser int!!")
finally:
    print("Chegamos ao fim!")

# Tratamento de exceções part 2
try:
    num = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))
    print(num/num2)
except ValueError:
    print("Numero deve ser int!!")
except ZeroDivisionError:
    print("Não divida por zero!!")
finally:
    print("Chegamos ao fim!")