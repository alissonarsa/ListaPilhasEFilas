def inverter_string(palavra):
    pilha = []

    for i in palavra:
        pilha.append(i)
        p_invertida = ""
    
    while pilha:
        p_invertida += pilha.pop()

    return p_invertida

print(inverter_string("Alisson"))