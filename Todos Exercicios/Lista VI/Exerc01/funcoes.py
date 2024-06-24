
def determinar_se_menor_valor_par(valor):
    menor_valor = min(valor)

    if menor_valor % 2 == 0:
        # print('O menor valor informado é par!')
        return 'O valor informado é par!'
    else:
        #print('O menor valor informado não é par!')
        return 'O valor informado não é par!'


