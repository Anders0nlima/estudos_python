v1 = int(input("Valor: "))


def comparar(v1):
    if v1 > 0:
        print(f"O valor: {v1} é maior que 0")   
    elif v1 < 0:
        print(f"O valor: {v1} é menor que 0")
    else:
        print(f"O valor: {v1} é igual a 0") 
        
comparar(v1)
