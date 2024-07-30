print('********* Média de Aproveitamento Conceito **********')

primeira_nota = input('Digite a primeira nota parcial: ')
segunda_nota = input('Digite a segunda nota parcial: ')

parcial_nota = float(primeira_nota)
parcial_segunda_nota = float(segunda_nota)

nota_final = (parcial_nota + parcial_segunda_nota) / 2 

if nota_final > 9.0 and nota_final == 10.0:
    print('Sua nota foi A, APROVADO!')
elif nota_final >= 7.5 and nota_final < 9.0:
    print('Sua nota foi B, APROVADO!')
elif nota_final == 6.0 and nota_final < 7.5:
    print('Sua nota foi C, APROVADO!')
elif nota_final >= 4.0 and nota_final < 6.0:
    print('Sua nota foi D, REPROVADO!')
else:
    print('Sua nota foi E, REPROVADO!')


print('A média é', nota_final)