def verifica_se_par_ou_impar(valores):
    valor_anterior = 0
    nova_lista = []

    for i, v in enumerate(valores):
        if v % 2 == 0:
            if i == 0:
                nova_lista.append(v + 2)
                valor_anterior = v
            else:
                nova_lista.append(v + valor_anterior)
                valor_anterior = v

        else:
            if i == 0:
                nova_lista.append(v - 1)
                valor_anterior = v
            else:
                nova_lista.append(v - valor_anterior)
                valor_anterior = v
    return nova_lista