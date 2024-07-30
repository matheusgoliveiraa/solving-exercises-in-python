peso = float(input('Digite o peso do peixe (kg): '))
excesso = 50
multa = 4.00

if peso > excesso:
    print('Você excedeu o peso, deve pagar uma multa de R$', multa, 'reais')
elif peso < excesso:
    print('O Kg do peixe, está dentro dos padrões')
elif peso == excesso:
    print('O Kg do peixe, está dentro dos padrões')