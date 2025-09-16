num = int(input("Digite um numero: "))


if num <= 0:
    print("Numero invalido")
else: 
    resultado = " "

    lista_romano = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    lista_normal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    num_origem = num

    for romano, normal in zip(lista_romano, lista_normal):
        while num >=  normal:
            resultado += romano
            num -= normal
    print(f"{num_origem} é igual a {resultado}")