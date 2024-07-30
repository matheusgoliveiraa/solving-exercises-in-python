print('##### VERIFICAÇÃO DE ANOS BISSEXTO #####')

from calendar import isleap

ano = float(input('Digite um ano: '))

if isleap(ano):
    print('É um ano bissexto!')
else:
    print('Não é bissexto!')