from funcoes import *

def test_lista_valores():
    entrada = [1, 2, 3, 4, 5]
    saida = lista_de_valores(entrada)
    assert saida == [2, 6, 6, 12, 10]
