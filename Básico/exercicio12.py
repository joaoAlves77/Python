'''
Faça um programa que declare uma lista vazia
e continue solicitando uma ação ao usuario
enquanto ele quiser continuar.

As ações são: Adicioar um tarefa à lista e
Remover uma tarefa da lista.

O programa deve imprimir a lista atualizada
toda vez antes da ação do usuario, algo como isso:
'''
lista = []
continua = "s"
print('lista atual:\n')
while(continua == 's'):
    print('o que deseja fazer?')
    print('1. Adicionar uma tarefa à lista;\n2. Remover uma tarefa à lista;')
    escolha = int(input('Escolha: ')) 

    if escolha == 1:
        item = input('Digite nome da tarefa: ')
        lista.append(item)
    elif escolha == 2:
        item = input('Digite nome da tarefa: ')
        lista.remove(item)
    else: 
        print('Invalido')   

    continua = input("Deseja continuar? (s/n): ")

print(lista)