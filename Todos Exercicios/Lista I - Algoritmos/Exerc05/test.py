from funcoes import *

def test_valor_sucessor_antecessor():
    valor = 20
    saida = valor_sucessor_e_antecessor(valor)
    assert saida == (21, 19)