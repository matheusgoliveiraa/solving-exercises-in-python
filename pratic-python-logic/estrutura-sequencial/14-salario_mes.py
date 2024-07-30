valorHora = float(input('Digite o valor hora: '))
horasTrabalhadas = float(input('Digite as horas trabalhadas no mês: '))
salario = float(input('Digite o seu salário: '))
inss = 8
impostoRenda = 11
sindicato = 5


salarioBruto = valorHora * horasTrabalhadas
descontoInss = (inss / 100) * salarioBruto
descontoSindicato = (sindicato / 100) * salarioBruto
descontoImposto = (impostoRenda / 100) * salarioBruto
salarioLiquido = round(salarioBruto - descontoSindicato - descontoImposto - descontoInss)

print('+ Salário Bruto: R$ ', salarioBruto)
print('- IR (11%): R$ ', impostoRenda)
print('- INSS (8%): R$ ', descontoInss)
print('- Sindicato (5%): R$ ', descontoSindicato)
print('= Salário Liquido: R$ ', salarioLiquido)

