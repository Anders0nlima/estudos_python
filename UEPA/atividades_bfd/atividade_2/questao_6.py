valor_por_hora = int(input("valor a hora: "))
horas_trabalhadas = int(input("horas de trabalho por dia: "))
mes = 30

horas_totais = horas_trabalhadas * mes 

salario = valor_por_hora * horas_totais

print(f"O salaria mensal é {salario}")