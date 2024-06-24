valor = float(input('Informe o valor de seu produto: '))
dias_atraso = int(input('Informe os dias de atraso: '))

multa = valor * 0.05 * dias_atraso
valor_final = valor + multa

print(f'O valor final a pagar é de R$: {valor_final}')