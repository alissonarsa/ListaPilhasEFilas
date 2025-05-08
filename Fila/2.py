from collections import deque

def verificar_palindromo(palavra):
    pilha = []
    fila = deque()

    for i in palavra:
        pilha.append(i)
        fila.append(i)

    while pilha:
        if pilha.pop() != fila.popleft():
            return False

    return True

print(verificar_palindromo("radar"))
print(verificar_palindromo("python"))
print(verificar_palindromo("ana"))