from collections import deque

class Impressora:
    def __init__(self):
        self.fila = deque() 

    def adicionar_documento(self, nome, paginas):
        self.fila.append({"nome": nome, "paginas": paginas})
        print(f"Documento '{nome}' com {paginas} páginas adicionado à fila")

    def imprimir_proximo(self):
        if not self.fila:
            print("Nenhum documento na fila para imprimir")
            return None
        documento = self.fila.popleft()  # Remove o próximo documento da fila
        print(f"Imprimindo '{documento['nome']}' com {documento['paginas']} páginas.")
        return documento

    def mostrar_fila(self):
        if not self.fila:
            print("A fila de impressão está vazia")
        else:
            print("Documentos na fila:")
            for doc in self.fila:
                print(f"- {doc['nome']} ({doc['paginas']} páginas)")


impressora = Impressora()
impressora.adicionar_documento("TrabProfAnderson", 10)
impressora.adicionar_documento("Relatório", 5)
impressora.adicionar_documento("Apresentação", 15)
impressora.mostrar_fila()
impressora.imprimir_proximo()
impressora.mostrar_fila()
impressora.imprimir_proximo()
impressora.imprimir_proximo()
impressora.imprimir_proximo()