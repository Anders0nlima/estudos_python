num = int(input("Seu numero: "))

if num > 0:
    soma = 0
    num_string = str(num)
    for i in range(len(num_string)):
        soma += int(num_string[i])
    print(soma)
else: 
    print("numero invalido")



