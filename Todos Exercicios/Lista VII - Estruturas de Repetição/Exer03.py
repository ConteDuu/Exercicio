populacao = int(input('Informe o número de habitantes: '))
taxa_cresc = float(input('Informe a taxa de crescimento da população: '))

taxa_cresc /= 100

for i in range(15):
    populacao *= 1 + taxa_cresc

print(f'A população da cidade, após 15 anos será de {populacao:.0f}')
