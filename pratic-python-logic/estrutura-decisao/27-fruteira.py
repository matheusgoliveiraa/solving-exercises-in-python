quantidade_morango = float(input('Quantidade de morangos em (Kg):'))
quantidade_macas = float(input('Quantidade de maças em (Kg): '))

valor_compra = 25
valor = 5

morango = 2.50
maca = 1.80


if quantidade_morango * morango > 8:
    print('O valor a ser pago pelos morangos é ', quantidade_morango * morango % 10)
