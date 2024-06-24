from funcoes import *

def test_area_quadrado():
    entrada = 10
    saida = calcula_area_quadrado(entrada)
    assert saida == 100

def test_area_circulo():
    entrada = 5
    saida = calcula_area_circulo(entrada)
    assert saida == 78.5


def test_area_triangulo():
    base = 10
    altura = 5
    saida = calcula_area_triangulo(base, altura)
    assert saida == 25