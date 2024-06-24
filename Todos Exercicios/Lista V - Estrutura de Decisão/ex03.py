x = int(input('Informe o primeiro número: '))
y = int(input('Informe o segundo número: '))
z = int(input('Informe o terceiro número: '))


if x > y and x >z:
    print(f'O maior é o valor: {x}')
elif y > x and y > z:
    print(f'O maior é o valor: {y}')
else:
    print(f'O maior é o valor: {z}')
    