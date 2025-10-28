salario = float(input("salario: "))

if salario >= 500:
    novo_salario = salario * 1.05
    print(novo_salario)
elif salario > 500 and salario < 1200:
    novo_salario = salario * 1.12
else: 
    novo_salario = salario



