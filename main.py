# Lista de tarefas
tarefas = []

# Função para adicionar tarefas
def adicionar_tarefa(tarefa):
    tarefas.append({"nome": tarefa, "status": "pendente"})
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

# Função para exibir tarefas
def exibir_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    for idx, tarefa in enumerate(tarefas, start=1):
        print(f"{idx}. {tarefa['nome']} - {tarefa['status']}")

# Função para alterar o status de uma tarefa
def alterar_status_tarefa(indice):
    if indice < 1 or indice > len(tarefas):
        print("Índice inválido!")
        return
    tarefa = tarefas[indice - 1]
    novo_status = "concluído" if tarefa["status"] == "pendente" else "pendente"
    tarefa["status"] = novo_status
    print(f"Tarefa '{tarefa['nome']}' marcada como {novo_status}.")

# Função para limpar a lista
def limpar_lista():
    dia = input("Digite o dia (dd/mm/aaaa) para registrar a limpeza: ")
    tarefas.clear()
    print(f"Lista de tarefas limpa em {dia}.")

# Menu principal
while True:
    print("\n1. Adicionar Tarefa\n2. Exibir Tarefas\n3. Alterar Status\n4. Limpar Lista\n5. Sair")
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
        limpar_lista()
    elif opcao == "5":
        break
    else:
        print("Opção inválida!")
