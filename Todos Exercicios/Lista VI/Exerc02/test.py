from funcoes import *

def test_calcula_porcentagem_votos():
    entrada1 = 1000
    entrada2 = 1300
    entrada3 = 4000
    saida = calcula_porcentagem_votos(entrada1, entrada2, entrada3)
    assert saida == (16, 21, 63)
