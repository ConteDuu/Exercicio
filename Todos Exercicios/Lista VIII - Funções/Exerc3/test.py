from funcoes import *


def test_soma_numeros_ate_valor():
    entrada = 3
    saida = soma_dos_numeros_ate_valor(entrada)
    assert saida == 6