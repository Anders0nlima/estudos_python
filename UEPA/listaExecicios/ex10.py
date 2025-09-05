num = int(input("Digite um numero: "))
if num <= 0:
    print("Numeros negativos são invalidos")
else:
    resultado = ""

    resultado += "OKOSA " * (num//2)

    if num % 2 != 0:
        resultado += "URAPUM"
     
    print("Tribo: ")
    print(resultado)