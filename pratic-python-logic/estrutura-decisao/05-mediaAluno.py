primeiraNota = float(input('Digite a primeira nota: '))
segundaNota = float(input('Digite a segunda nota: '))

media = (primeiraNota + segundaNota) / 2

if media >= 7 and media <= 9:
    print('Aprovado')
elif media < 7:
    print('Reprovado')
elif media == 10:
    print('Aprovado com Distincao')

