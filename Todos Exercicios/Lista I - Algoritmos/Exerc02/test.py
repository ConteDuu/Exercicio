from funcoes import *

def test_calcu_salario_total():
    salario = 2000
    aumento = 15

    saida = calcula_aumento(salario, aumento)
    assert saida == 2300