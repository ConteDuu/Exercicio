def valores_posicao_par(valores):
    soma = []
    for ind, num in enumerate(valores):
        if ind % 2 == 0:
            soma.append(num)
    return soma