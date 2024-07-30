pinturaArea = int(input('Qual tamanho em metros, da área a ser pintada?: '))
lataTinta = 18
metros = 3
preco = 80

quantidadeTinta = round(pinturaArea / metros / lataTinta)
valorTotal = quantidadeTinta * preco

print('A quantidade de tinta a ser utilizada é: ', quantidadeTinta)
print('O valor total a ser gasto é: R$ ', valorTotal)
