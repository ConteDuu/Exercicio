# Alunos participantes: Eduardo Conte, Vitor Gabriel Conte, Henrique Trentin 


metros_gastos = float(input('Informa qunatos m³ foram gastos: '))
fixo = 34.49

if metros_gastos <= 5:
    print(f'O valor da fatura é: {fixo}')
else:

    # Faixa 1 - 6 a 10 m³
    if metros_gastos >= 6 and metros_gastos <= 10:

        m_total1 = metros_gastos - 5 
        metros_total1 = m_total1*1.07 + fixo 

        print(f'O valor a pagar é de: {metros_total1}') 

    # Faixa 2 - 11 a 15 m³
    elif metros_gastos >= 11 and metros_gastos <= 15:

        m_total2 = metros_gastos - 10
        m_total3 = 5*1.07 
        metros_total2 = m_total2*5.94 + fixo + m_total3
        print(f'o valor da fatura é de: {metros_total2:.2f}')   

    # Faixa 3 - 16 a 20 m³
    elif metros_gastos >= 16  and metros_gastos <= 20:

        m_total2 = metros_gastos - 15 
        m_total3 = fixo + 5*1.07 + 5*5.94
        metros_total2 = m_total2*5.97 + m_total3

        print(f'o valor da fatura é de: {metros_total2}')  
    # Faixa 4 - 21 a 30 m³
    elif metros_gastos >= 21  and metros_gastos <= 30:

        m_total2 = metros_gastos - 20 
        m_total3 = fixo + 5*1.07 + 5*5.94 + 5*5.97
        metros_total2 = m_total2 * 6.02 + m_total3

        print(f'o valor da fatura é de: {metros_total2}') 
    # Faixa 5 - Acima de 30
    else:
        m_total2 = metros_gastos - 30 
        m_total3 = fixo + 5*1.07 + 5*5.94 + 5*5.97 + 10*6.02
        metros_total2 = m_total2 * 10.19 + m_total3

        print(f'o valor da fatura é de: {metros_total2}') 




