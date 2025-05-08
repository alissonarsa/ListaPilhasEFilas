class EditorTexto:
    def __init__(self):
        self.pilha_acoes = [] 

    def adicionar_acao(self, acao):
        self.pilha_acoes.append(acao)
        print(f"Ação adicionada: {acao}")

    def desfazer(self):
        if not self.pilha_acoes:
            print("Nada para desfazer")
            return None
        ultima_acao = self.pilha_acoes.pop()
        print(f"Ação desfeita: {ultima_acao}")
        return ultima_acao


editor = EditorTexto()
editor.adicionar_acao("Alisow 123")
editor.adicionar_acao("Alishow 456")
editor.desfazer()
editor.desfazer()
editor.desfazer()  