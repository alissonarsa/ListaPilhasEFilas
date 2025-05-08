def avaliar_posfixa(expressao):
    pilha = []
    operadores = {'+': lambda x, y: x + y, # funções anonimas
                  '-': lambda x, y: x - y,
                  '*': lambda x, y: x * y,
                  '/': lambda x, y: x / y}

    tokens = expressao.split()

    for token in tokens:
        if token.isdigit(): #verif. se é inteiro
            pilha.append(int(token))
        elif token in operadores:
            b = pilha.pop()
            a = pilha.pop()
            resultado = operadores[token](a, b)
            pilha.append(resultado)
        else:
            raise ValueError(f"Token inválido: {token}") # exceção

    return pilha.pop()

print(avaliar_posfixa("2 3 +"))
print(avaliar_posfixa("5 1 2 + 4 * + 3 -"))