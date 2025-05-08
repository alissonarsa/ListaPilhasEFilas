class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.fila = [None] * capacidade
        self.inicio = 0
        self.fim = -1
        self.tamanho = 0

    def enfileirar(self, elemento):
        if self.tamanho == self.capacidade:
            print("A fila está cheia!")
            return False
        self.fim = (self.fim + 1) % self.capacidade
        self.fila[self.fim] = elemento
        self.tamanho += 1
        return True

    def desenfileirar(self):
        if self.tamanho == 0:
            print("A fila está vazia!")
            return None
        elemento = self.fila[self.inicio]
        self.fila[self.inicio] = None
        self.inicio = (self.inicio + 1) % self.capacidade
        self.tamanho -= 1
        return elemento

    def mostrar_fila(self):
        print("Fila:", self.fila)


fila = FilaCircular(5)
fila.enfileirar(10)
fila.enfileirar(20)
fila.enfileirar(30)
fila.mostrar_fila()
print(f"Desenfileirado: {fila.desenfileirar()}")
fila.mostrar_fila()
fila.enfileirar(40)
fila.enfileirar(50)
fila.enfileirar(60)
fila.mostrar_fila()
fila.enfileirar(70) 