from funcoes import *

def test_calcula_valor():
    entrada = 10.5
    saida = dobro_valor(entrada)
    assert saida == 21
