import math
num = int(input("Numero: "))
base = int(input("Base: "))

if num > 0:
    resultado = math.log(num, base)
    print(resultado)
else:
    print("numero invalido")
