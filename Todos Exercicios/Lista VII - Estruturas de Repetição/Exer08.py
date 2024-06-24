dividendo = int(input('Informe o valor a ser dividido: '))
divisor = int(input('Informe o valor divisor: '))

resultado = 0
while dividendo >= divisor:
    dividendo -= divisor
    resultado += 1

print(f'O resto da divisão é: {dividendo}')
print(f'O resultado da divisão é: {resultado}')