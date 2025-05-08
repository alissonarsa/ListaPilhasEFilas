from collections import deque

class FilaAtendimento:
    def __init__(self):
        self.fila = deque()

    def adicionar_cliente(self, cliente):
        self.fila.append(cliente)
        print(f"Cliente {cliente} entrou na fila.")

    def atender_cliente(self):
        if not self.fila:
            print("Nenhum cliente na fila para atender.")
            return None
        cliente = self.fila.popleft()
        print(f"Cliente {cliente} foi atendido.")
        return cliente

    def mostrar_fila(self):
        if not self.fila:
            print("A fila está vazia.")
        else:
            print("Clientes na fila:", list(self.fila))


fila = FilaAtendimento()
fila.adicionar_cliente("João")
fila.adicionar_cliente("Maria")
fila.adicionar_cliente("Carlos")
fila.mostrar_fila()
fila.atender_cliente()
fila.mostrar_fila()
fila.atender_cliente()
fila.atender_cliente()
fila.atender_cliente()