num = int(input("digite um numero:"))

i = 1 
cont = 0
soma = 0

print(num,"**2 = ", end=" ")

while cont < num: 
    soma += i 
    print(i, end =" ")
    cont += 1 
    i += 2
    if cont < num:
        print(" + ", end = "")
print(" = ", soma)   


