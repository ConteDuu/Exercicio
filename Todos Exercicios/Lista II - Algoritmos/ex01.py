idade = int(input('Qual a sua idade? '))

if idade < 16:
    print('Você não pode votar nem dirigir!')

elif idade >= 16 and idade < 18:
        print('Você já pode votar, mas não dirigir!') 
        
else:
     print('Você já pode votar e pode dirigir')


