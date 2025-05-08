import heapq

class FilaDePrioridade:
    def __init__(self):
        self.fila = []

    def adicionar_tarefa(self, prioridade, tarefa):
        heapq.heappush(self.fila, (prioridade, tarefa))
        print(f"Tarefa '{tarefa}' com prioridade {prioridade} adicionada à fila")

    def remover_tarefa(self):
        if not self.fila:
            print("A fila está vazia")
            return None
        prioridade, tarefa = heapq.heappop(self.fila)
        print(f"Tarefa '{tarefa}' com prioridade {prioridade} removida da fila")
        return tarefa

    def mostrar_fila(self):
        if not self.fila:
            print("A fila está vazia")
        else:
            print("Tarefas na fila (prioridade, tarefa):")
            for item in sorted(self.fila):
                print(f"- Prioridade {item[0]}: {item[1]}")

fila = FilaDePrioridade()
fila.adicionar_tarefa(3, "Tarefa C")
fila.adicionar_tarefa(1, "Tarefa A")
fila.adicionar_tarefa(2, "Tarefa B")
fila.mostrar_fila()
fila.remover_tarefa()
fila.mostrar_fila()
fila.remover_tarefa()
fila.remover_tarefa()
fila.remover_tarefa()