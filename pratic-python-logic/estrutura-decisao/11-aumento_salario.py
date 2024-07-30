salario = float(input("Digite o seu salário: "))

if salario <= 280:
    percentual = 20
elif salario <= 700:
    percentual = 15
elif salario <= 1500:
    percentual = 10
else:
    percentual = 5


percentual = round(percentual/100, 2)
aumento = round(salario * percentual, 2)
salario_reajustado = round(salario + aumento, 2)

print("O seu salário antes do reajuste é: ", salario)
print("O percentual de aumento aplicado: ", percentual)
print("O valor do aumento: ", aumento)
print("O novo salario, após o aumento: ", salario_reajustado)
