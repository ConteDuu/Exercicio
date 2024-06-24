from funcoes import *

def test_valor_ate_informado():
    entrada = 3
    saida = soma_ate_valor_informado(entrada)
    assert saida == 6