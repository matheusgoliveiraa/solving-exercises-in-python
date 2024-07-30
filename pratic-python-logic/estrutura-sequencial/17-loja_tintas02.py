area = int(input('Qual o tamanho em metros, da área a ser pintada?: '))
metros = 6
lataTinta = 18
precoLata = 80

galoes = 3.6
valorGaloes = 25


quantidadeTinta = round(area / metros / lataTinta)

print('A quantidade de latas de tinta é: ', quantidadeTinta)

if quantidadeTinta >= 18:
    print('comprar apenas ', lataTinta, 'litros', 'e o preco e', precoLata, 'R$')
elif quantidadeTinta< 18:
    print('comprar apenas', galoes, 'litros', 'e o preco e', valorGaloes, 'R$')