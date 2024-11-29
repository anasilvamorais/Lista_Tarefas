# main.py
tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append({"nome": tarefa, "status": "pendente"})
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def exibir_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    for idx, tarefa in enumerate(tarefas, start=1):
        print(f"{idx}. {tarefa['nome']} - {tarefa['status']}")
