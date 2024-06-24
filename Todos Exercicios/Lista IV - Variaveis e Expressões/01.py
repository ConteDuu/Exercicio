total_prestacoes = int(input('Qual a quantidade total de prestações tem a pagar? '))
quant_prestacoes = int(input('Quantas prestações já foram pagas? '))
valor_prestacao = float(input('Qual o valor de cada prestação? '))

total_pago = valor_prestacao * quant_prestacoes
saldo_devedor = total_prestacoes * valor_prestacao - total_pago
print(f'O valor pago até o momento é de: R${total_pago}reais e o saldo devedor é de: R${saldo_devedor} reais.')