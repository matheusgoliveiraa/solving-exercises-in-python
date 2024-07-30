primeiro_bimestre = float(input('Digite a primeira nota: '))
segundo_bimestre = float(input('Digite a segunda nota: '))
terceiro_bimestre = float(input('Digite a terceira nota: '))
quarto_bimestre = float(input('Digite a quarta nota: '))

media = (primeiro_bimestre + segundo_bimestre + terceiro_bimestre + quarto_bimestre) / 4

if (media < 7.0):
    print('Você foi reprovado, com a nota final', media)
elif (media > 7.0):
    print('Você foi aprovado, com a nota final', media)
