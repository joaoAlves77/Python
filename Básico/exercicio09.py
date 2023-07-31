'''
Faça um programa que receba as medidas dos três 
lados de um triangulo e diga se ele é equilatero, isosceles
ou escaleno

# Equilátero: Todos os lados iguais
# Escaleno: Possui 2 lados iguais
# Isosceles: Todos os lados diferentes 
'''
l1 = int(input("digite lado 1 do triangulo: "))
l2 = int(input("digite lado 2 do triangulo: "))
l3 = int(input("digite lado 3 do triangulo: 3"))

if(l1 == l2 and l2 == l3):
    print("Triângulo é equilátero")
elif(l1 != l2 and l2 != l3):
    print("Triângulo é Escaleno")
else:
    print("Triângulo é Isosceles")