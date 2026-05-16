num = int(input("Digite um numero: "))

if num <= 0:
    print("numeros iguais ou iguais a zero são invalidos")
else:
    resultado = " "
    resultado += "OKASA " * (num//2)

    if num % 2 != 0:
        resultado += "URAPUM "

print(resultado)