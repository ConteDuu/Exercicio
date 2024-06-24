from funcoes import * 

# 1 maneira
def test_maior_numero():
    valor1, valor2 = 10, 20
    saida = numeros_inteiros(valor1, valor2)
    assert saida == 10

# 2 maneira
def test_maior_numero_test():
    valor1, valor2 = 10, 20
    saida = numeros_inteiros_teste(valor1, valor2)
    assert saida == 20