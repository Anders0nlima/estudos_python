print("""
digite uma operção:
1- soma
2- subtração
3- divisão
4- multiplicação
""")


operedor = int(input("operação: "))
num1 = int(input("primeiro numero: "))
num2 = int(input("segundo numero: "))

if operedor == 1:
    print(num1 + num2)
elif operedor == 2:
    print(num1 - num2)
elif operedor == 3:
    if num2 == 0:
        print("Invalido")
    else:
        print(num1 / num2) 
elif operedor == 4:
    print(num1 * num2)
else:
    print("Operador não valido")

