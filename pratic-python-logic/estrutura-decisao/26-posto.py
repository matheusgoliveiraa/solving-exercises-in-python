combustivel_alcool = float(input('Quantos litros de combustível ( alcool ): '))
combustivel_gasolina = float(input('Quantos livros de combustível ( gasolina ): '))
alcool = 20
desconto_alcool = 3

gasolina = 20
desconto_gasolina = 4

preco_gasolina = 2.50
preco_alcool = 1.90


if combustivel_alcool <= alcool:
    print('A. Alcool - O valor do combustivel do alcool a ser pago é R$: ', combustivel_alcool * preco_alcool - desconto_alcool)
else:
    print('A. Alcool - O valor do combustivel do alcool a ser pago é R$: ', combustivel_alcool * preco_alcool - 6)

if combustivel_gasolina <= gasolina:
    print('G. Gasolina - O valor do combustível dá gasolina a ser pago é R$: ', combustivel_gasolina * preco_gasolina - desconto_gasolina)
else:
    print('G. Gasolina - O valor do combustível da gasolina a ser pago é R$: ', combustivel_gasolina * preco_gasolina - 6)


