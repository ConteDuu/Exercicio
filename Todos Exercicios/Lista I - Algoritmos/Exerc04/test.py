from funcoes import  *

def test_calcula_volume_caixa():
    comprimento = 30
    largura = 20
    altura = 15

    saida = calcula_valume_caixa(comprimento, largura, altura)
    assert saida == 9000
