num = int(input("Numero: "))

while num % 2 == 0:
    num = num // 2

if num == 1:
    print("é potencia de 2")
else:
    print("não é potencia de 2")