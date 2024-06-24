def calcula_porcentagem_votos(candidato1, candidato2, candidato3):
    total_votos = candidato1 + candidato2 + candidato3
    votos_candidato1 = candidato1 * 100 / total_votos
    votos_candidato2 = candidato2 * 100 / total_votos
    votos_candidato3 = candidato3 * 100 / total_votos
    return round(votos_candidato1), round(votos_candidato2), round(votos_candidato3)