positivos = 0

resposta = input('a. Telefonou para a vítima? (Sim ou Não): ')
if resposta == 'Sim':
    positivos += 1
resposta = input('b. Esteve no local do crime? (Sim ou Não): ')
if resposta == 'Sim':
    positivos += 1
resposta = input('c. Mora perto da vítima? (Sim ou Não): ')
if resposta == 'Sim':
    positivos += 1
resposta = input('d. Devia para a vítima? (Sim ou Não): ')
if resposta == 'Sim':
    positivos += 1
resposta = input('e. Já trabalhou com a vítima? (Sim ou Não): ')
if resposta == 'Sim':
    positivos += 1

if positivos < 2:
    print('Inocente!')
elif positivos == 2:
    print('Suspeito!')

elif positivos == 3 or positivos == 4:
    print('Cúmplice')
else:
    print('Assassino!')