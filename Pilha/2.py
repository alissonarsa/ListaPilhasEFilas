def verifica_balanceamento(expressao):
    pilha = []
    pares = {')': '(', ']': '[', '}': '{'}

    for i in expressao:
        if i in "([{":
            pilha.append(i)
        elif i in ")]}":
            if not pilha or pilha[-1] != pares[i]:
                return False
            pilha.pop() 

    return not pilha

print(verifica_balanceamento("{[()]}")) 
print(verifica_balanceamento("{[(])}"))