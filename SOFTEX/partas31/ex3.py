try:
    num = int(input("Digite um numero: "))
    lista_num = []
    for i in range(1, num):
        if num%i == 0:
            lista_num.append(i)


    soma = sum(lista_num)
    if soma == num:
        print(f"O número {num} é perfeito")  
    else:
        print(f"O numero {num} não é perfeito")  

except ValueError:
    print("Digite um numero")

