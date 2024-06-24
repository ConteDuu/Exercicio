from funcoes import *

def test_valor_menor_par():
    valor = [10]
    saida = determinar_se_menor_valor_par(valor)
    assert saida == 'O valor informado é par!'