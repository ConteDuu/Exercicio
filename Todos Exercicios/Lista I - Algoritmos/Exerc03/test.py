from funcoes import *

def test_idade_apos_periodo():
    idade = 30
    periodo = 15

    saida = idade_apos_periodo(idade, periodo)
    assert saida == 45