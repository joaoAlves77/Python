tarefas = []

while True:
    print("======= LISTA DE TAREFAS =======")
    print("1 - Adicionar tarefa")
    print("2 - Ver lista de tarefas")
    print("3 - Remover tarefa")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        tarefa = input("Digite a nova tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")
   
    elif opcao == "2":
        if not tarefas:
            print("Não há tarefas na lista.")
        else:
            print("Lista de tarefas:")
            for i, tarefa in enumerate(tarefas):
                print(f"{i+1}. {tarefa}")

    elif opcao == "3":
            if not tarefas:
                print("Não há tarefas para remover.")
            else:
                tarefa = int(input("Digite o número da tarefa que deseja remover: "))
                try:
                     if tarefa > 0 and tarefa <= len(tarefas):
                        tarefas.pop(tarefa-1)
                        print("Tarefa removida com sucesso!")
                     else:
                        print("Opção inválida.")
                except ValueError:
                    print("Opção inválida.")

    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")