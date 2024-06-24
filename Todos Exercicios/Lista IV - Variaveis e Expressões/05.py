# Entrada dos valores da conta e do valor fornecido pelo usuário
valor_conta = float(input("Digite o valor da conta: "))
valor_fornecido = float(input("Digite o valor fornecido pelo cliente: "))

# Calculando o troco
troco = valor_fornecido - valor_conta

# Calculando a quantidade de cada tipo de cédula no troco
cédulas100 = 0
cédulas10 = 0
cédulas1 = 0

if troco >= 100:
    cédulas100 = int(troco / 100)
    troco -= cédulas100 * 100

if troco >= 10:
    cédulas10 = int(troco / 10)
    troco -= cédulas10 * 10

if troco >= 1:
    cédulas1 = int(troco / 1)
    troco -= cédulas1 * 1

# Saída do resultado
print("\nValor da compra:", valor_conta)
print("Valor do troco:", valor_fornecido - valor_conta)
print("\nQuantidade de cédulas de R$ 100:", cédulas100)
print("Quantidade de cédulas de R$ 10:", cédulas10)
print("Quantidade de cédulas de R$ 1:", cédulas1)

