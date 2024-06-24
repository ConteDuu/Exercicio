def calculo_gasto_internet(mbs=float):
    total_gasto = mbs * 0.50
    return total_gasto


def calculo_ligacao_local(min=float):
    total_gasto = min * 0.35
    return total_gasto


def calculo_ligacao_interurbana(min=float):
    total_gasto = min * 0.60
    return total_gasto


def calculo_torpedo(torpedos=int):
    total_gasto = float(torpedos * 0.20)
    return total_gasto


def calcular_fatura(internet, ligacao_local, ligacao_interurbana, torpedo):
    # Calcula o custo de cada serviço
    custo_internet = internet* 0.50
    custo_ligacao_local = ligacao_local * 0.35
    custo_ligacao_interurbana = ligacao_interurbana * 0.60
    custo_torpedo = torpedo * 0.20

    # Calcula o total da fatura sem desconto
    total_sem_desconto = custo_internet + custo_ligacao_local + custo_ligacao_interurbana + custo_torpedo

    # Aplica os descontos
    desconto = 0
    tipo_desconto = "Nenhum"

    if internet > 50:
        desconto = total_sem_desconto * 0.05
        tipo_desconto = "Internet"
    if ligacao_local > 200:
        desconto = total_sem_desconto * 0.10
        tipo_desconto = "Ligações locais"
    if ligacao_interurbana > 150:
        desconto = total_sem_desconto * 0.10
        tipo_desconto = "Ligações interurbanas"
    if torpedo > 50:
        desconto = total_sem_desconto * 0.20
        tipo_desconto = "Torpedos"

    # Calcula o total da fatura com desconto
    total_com_desconto = total_sem_desconto - desconto

    return total_sem_desconto, tipo_desconto, desconto, total_com_desconto

