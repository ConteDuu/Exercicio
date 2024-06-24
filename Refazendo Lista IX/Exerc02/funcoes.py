def lista_de_valores(valores):
    nova_lista = []
    for i, v in enumerate(valores):
        if i %2 == 0:
            nova_lista.append(v *2)
        else:
            nova_lista.append(v * 3)
    return nova_lista