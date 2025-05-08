def convert_p_binarios(numero):
    pilha = []

    while numero > 0:
        resto = numero % 2
        pilha.append(resto)
        numero = numero // 2

    binario = ""
    while pilha:
        binario += str(pilha.pop())
    
    return binario
    
print(convert_p_binarios(10))

