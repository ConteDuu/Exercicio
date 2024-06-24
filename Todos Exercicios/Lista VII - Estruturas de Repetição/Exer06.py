num = int(input('Informe um número: '))

metade_num = num // 2
primo = True

for i in range(2, metade_num + 1):
    if num % i == 0:
      primo = False
      break

if primo:
  print('O valor inserido é primo!')
else: 
  print('O valor inserido não é primo!')