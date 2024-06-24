from funcoes import *

def test_valor_par_ou_impar():
    entrada = [1, 2, 3, 4]
    saida = verifica_se_par_ou_impar(entrada)
    assert saida == [3]