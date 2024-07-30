turno = input('Em qual turno você estuda?: ')
m = 'M- Matutino'
v = 'V- Vespertino'
n = 'N- Noturno'

if turno == m:
    print('Bom Dia!')
elif turno == v:
    print('Boa Tarde!')
else:
    if turno == n:
        print('Boa Noite!')
    else:
        print('Valor inválido!')


