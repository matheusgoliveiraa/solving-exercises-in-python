print('*********# Caixa Eletrônico #**********')

valor_saque = int(input('Qual o valor do saque? [Entre 10 e 600]: '))
valor_minimo = 10
valor_maximo = 600

cem = int(valor_saque / 100)
valor_saque = valor_saque - (cem*100)

cinquenta = int(valor_saque / 50)
valor_saque = valor_saque - (cinquenta*50)

dez = int(valor_saque / 10)
valor_saque = valor_saque - (dez*10)

cinco = int(valor_saque / 5)
valor_saque = valor_saque - (cinco*5)

um = valor_saque

print('Notas R$100,00 = ', cem)
print('Notas R$50,00 = ', cinquenta)
print('Notas R$10,00 = ', dez)
print('Notas R$5,00 = ', cinco)
print('Notas R$1,00 = ', um)


