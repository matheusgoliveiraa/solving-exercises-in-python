print('########## MÉDIA ALUNO ##########')

nota = float(input('Digite a sua N1: '))
nota_2 = float(input('Digite a sua N2: '))
nota_3 = float(input('Digite a sua N3: '))

media = (nota + nota_2 + nota_3) / 3

if media >= 7 and media < 10:
    print('Parabéns, você foi aprovado com a média: ', round(media, 1))
elif media < 7:
    print('Você foi reprovado, com a média: ', round(media, 1))
elif media == 10:
    print('Aprovado com Distinção, com a média: ', round(media, 1))