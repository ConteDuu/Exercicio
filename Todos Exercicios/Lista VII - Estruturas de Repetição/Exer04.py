for i in range(10):
    num = int(input('Informe um número: '))

    if num > num:
        maior = num
        menor = num

    elif num > maior:
        maior = num
    
    elif num < menor:
        menor = num

print(f'O maior número informado foi {maior}')
print(f'O maior número informado foi {menor}')


# Para eliminar o primeiro if podemos usar o 'sys.maxsize', que define o maior ou o menor numero possivel em python

import sys

maior = -sys.maxsize
menor = sys.maxsize

for i in range(10):
    num = int(input('Informe um número: '))


    if num > maior:
        maior = num
    
    elif num < menor:
        menor = num

print(f'O maior número informado foi {maior}')
print(f'O maior número informado foi {menor}')
