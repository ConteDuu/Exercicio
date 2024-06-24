soma_idade = 0
cont_homens = 0
cont_mulheres = 0
maior_idade = 0
sexo_maior_idade = ''

#-------------------------------------------------------------
for i in range(3):

    while True:
        sexo = input('Informe seu sexo com M para Masculino e F para Feminino: ').upper()
        if sexo  in ('M', 'F'):
            break
    print('Valor inválido para sexo! Informe M ou F!')


    while True:  
        idade = int(input('Informe sua idade: '))
        if idade <= 0:
            break
    print('Valor inválido para idade! Informe a idade correta!')

#-------------------------------------------------------------
    soma_idade += idade
    media_idade = soma_idade / i

#-------------------------------------------------------------
    if sexo == 'M':
        cont_homens += 1
    else:
        cont_mulheres += 1

    if idade > maior_idade:
        maior_idade = idade
        sexo_maior_idade = sexo



print(f'A média de idade das pessoas é {media_idade}')
print(f'O número de homens é de {cont_homens}')
print(f'O númeor de mulheres é de {cont_mulheres}')

