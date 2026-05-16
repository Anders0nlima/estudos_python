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

#print(lista_num)
#print(soma)



#(1+2+3=6)  6/1 = 6 6/2 = 3 6/3 = 2 6/4 = x.x

