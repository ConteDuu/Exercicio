from funcoes import *

def test_calcula_media():
    nota1, nota2, nota3, nota4 = 1, 5, 6, 8

    saida = culcula_media_aluno(nota1, nota2, nota3, nota4)
    assert saida == 3.05