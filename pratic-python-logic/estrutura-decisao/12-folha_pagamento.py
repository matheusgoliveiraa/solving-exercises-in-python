valor_hora = float(input('Digite o valor hora: '))
horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas: '))

salario_bruto = valor_hora * horas_trabalhadas


if (salario_bruto <= 900):
    desconto_ir = 0.0
elif (salario_bruto <= 1500):
    desconto_ir = 5
elif (salario_bruto <= 2500):
    desconto_ir = 10
else:
    desconto_ir = 20

ir = salario_bruto * (desconto_ir / 100)
inss = salario_bruto * (10 / 100)
fgts = salario_bruto * (11 / 100)

total_de_descontos = ir + inss
salario_liquido = salario_bruto - total_de_descontos

print(
    f"\nSalário Bruto     : R${salario_bruto:.2f}",
    f"\n(-) IR (5%)       : R${ir:.2f}",
    f"\n(-) INSS ( 10%)   : R${inss:.2f}",
    f"\nFGTS (11%)        : R${fgts:.2f}",
    f"\nTotal de descontos: R${total_de_descontos:.2f}",
    f"\nSalário Liquido   : R${salario_liquido:.2f}",
)

