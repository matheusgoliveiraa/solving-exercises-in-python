mb = int(input('Qual o tamanho do arquivo para download? em ( MB ) : '))
mbps = int(input('Qual a velocidade da internet? em ( Mbps ) : '))

velocidade = mb / (mbps / 8)

print('O tempo aproximado de download do arquivo e: ', velocidade)