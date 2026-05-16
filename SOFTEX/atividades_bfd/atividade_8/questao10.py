v1 = int(input("1- Valor: "))
v2 = int(input("2- Valor: "))


def comparar(v1, v2):
    if v1 > v2:
        print(f"O numero {v1} é maior que o {v2}")
    else:
        print(f"O numero {v2} é maior que o {v1}")
        
comparar(v1, v2)