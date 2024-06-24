from funcoes import *

def teste_valor_posicao_par():
    entrada = [1, 4, 3, 8, 3, 20, 54, 6, 7, 56]
    saida = valores_posicao_par(entrada)
    assert saida == [1, 3, 3, 54, 7]