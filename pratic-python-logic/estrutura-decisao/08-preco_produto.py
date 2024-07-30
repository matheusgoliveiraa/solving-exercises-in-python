primeiro_produto = float(input('Qual o preço, do produto N1: '))
segundo_produto = float(input('Qual o preço, do produto N2: '))
terceiro_produto = float(input('Qual o preço, do produto N3: '))

if primeiro_produto < segundo_produto:
    print('Esse é o menor preco, comprar o produto no valor de R$: ', primeiro_produto)
elif segundo_produto < terceiro_produto:
    print('Esse é o menor preco, comprar o produto no valor de R$: ', segundo_produto)
elif terceiro_produto < primeiro_produto:
     print('Esse é o menor preco, comprar o produto no valor de R$: ', terceiro_produto)


