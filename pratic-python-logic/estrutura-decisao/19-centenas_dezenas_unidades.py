valor = int(input('Digite um número inteiro: '))
unidade = valor % 10

valor = (valor - unidade) / 10
dezena = valor % 10

valor = (valor - dezena) / 10
centena = valor

dezena = int(dezena)
centena = int(centena)

print(centena, 'centena, ',dezena, 'dezena e ', unidade, 'unidade')
