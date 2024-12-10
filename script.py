class Tarefa:
    def __init__(self):
        # Duas listas paralelas: uma para os nomes das tarefas e outra para os estados (pendente ou concluída)
        self.tarefas = []
        self.estados = []

    def adicionar_tarefa(self, tarefa):
        """Adiciona uma tarefa à lista com o estado 'pendente'"""
        self.tarefas.append(tarefa)
        self.estados.append("pendente")

    def marcar_concluida(self, tarefa):
        """Marca uma tarefa como concluída"""
        if tarefa in self.tarefas:
            indice = self.tarefas.index(tarefa)
            self.estados[indice] = "concluída"
        else:
            print("Tarefa não encontrada.")

    def remover_tarefa(self, tarefa):
        """Remove uma tarefa da lista"""
        if tarefa in self.tarefas:
            indice = self.tarefas.index(tarefa)
            self.tarefas.pop(indice)
            self.estados.pop(indice)
        else:
            print("Tarefa não encontrada.")

    def listar_tarefas(self):
        """Lista todas as tarefas, mostrando o estado (pendente ou concluída)"""
        for tarefa, estado in zip(self.tarefas, self.estados):
            print(f"{tarefa} - {estado}")

    def pesquisar_tarefa(self, nome):
        """Pesquisa uma tarefa pelo nome"""
        if nome in self.tarefas:
            indice = self.tarefas.index(nome)
            print(f"Tarefa: {self.tarefas[indice]}, Estado: {self.estados[indice]}")
        else:
            print("Tarefa não encontrada.")

# Exemplo de uso
tarefa_manager = Tarefa()

# Adicionando tarefas
tarefa_manager.adicionar_tarefa("Estudar Python")
tarefa_manager.adicionar_tarefa("Fazer compras")

# Listando tarefas
print("Tarefas após adição:")
tarefa_manager.listar_tarefas()

# Marcando uma tarefa como concluída
tarefa_manager.marcar_concluida("Estudar Python")

# Listando tarefas novamente
print("\nTarefas após marcar uma como concluída:")
tarefa_manager.listar_tarefas()

# Pesquisando uma tarefa
print("\nPesquisando uma tarefa:")
tarefa_manager.pesquisar_tarefa("Fazer compras")

# Removendo uma tarefa
tarefa_manager.remover_tarefa("Fazer compras")

# Listando tarefas após remoção
print("\nTarefas após remoção:")
tarefa_manager.listar_tarefas()
