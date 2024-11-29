def alterar_status_tarefa(indice):
    if indice < 1 or indice > len(tarefas):
        print("Índice inválido!")
        return
    tarefa = tarefas[indice - 1]
    novo_status = "concluído" if tarefa["status"] == "pendente" else "pendente"
    tarefa["status"] = novo_status
    print(f"Tarefa '{tarefa['nome']}' marcada como {novo_status}.")

while True:
    print("\n1. Adicionar Tarefa\n2. Exibir Tarefas\n3. Alterar Status\n4. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        adicionar_tarefa(tarefa)
    elif opcao == "2":
        exibir_tarefas()
    elif opcao == "3":
        exibir_tarefas()
        indice = int(input("Digite o número da tarefa para alterar o status: "))
        alterar_status_tarefa(indice)
    elif opcao == "4":
        break
    else:
        print("Opção inválida!")
