cliente_insento = int(input('Quantos clientes estão insentos de pendências: '))
clientes_em_dia = int(input('Quantos clientes estão com as pendências em dia: '))
clientes_atraso = int(input('Quantos clientes estão com pendênciasa atrasadas: '))

total_cliente = cliente_insento + clientes_em_dia + clientes_atraso

porc_clientes_insentos = round(100 * cliente_insento / total_cliente, 2)

porc_cliente_dia = round(100 * clientes_em_dia / total_cliente, 2)

porc_cliente_atraso = round(100 * clientes_atraso / total_cliente, 2)

print(f'O total de clientes isentos de pend~encia é de: {porc_clientes_insentos}% \n O total de clientes com pendências em dia é de: {porc_cliente_dia}% \nO total de clientes com pendências atrasadas é de: {porc_cliente_atraso}%')
