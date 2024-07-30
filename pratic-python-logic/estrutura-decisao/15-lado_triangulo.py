primeiro_lado = int(input('Digite o primeiro um lado do triângulo: '))
segundo_lado = int(input('Digite o segundo lado do triângulo: '))
terceiro_lado = int(input('Digite o terceiro lado do triângulo: '))

if (primeiro_lado == segundo_lado == terceiro_lado):
    print('É um triângulo Equilátero!')
elif (primeiro_lado == segundo_lado):
    print('É um triângulo Isósceles!')
elif (primeiro_lado != segundo_lado != terceiro_lado):
    print('É um triângulo Escaleno!')


