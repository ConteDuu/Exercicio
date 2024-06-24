largura = float(input('Informe a largura do pacote em centímetros: '))
altura = float(input('Informe a altura do pacote: '))
comprimento = float(input('Informe a comprimento do pacote: '))

medida_barbante = largura + comprimento + 20

print(f'A medida necessária para amarar o pacote com duas volta é de: {medida_barbante} cm.')