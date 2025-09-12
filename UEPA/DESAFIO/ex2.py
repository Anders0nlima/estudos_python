num = input("digite um numero: ")
numinvertido = int(num)
print(num)

inverso = num[::-1]
resultadoinvertido = int(inverso)
print(inverso)


soma = numinvertido + resultadoinvertido


soma = str(soma)

while (True):
    if soma == soma[::-1]:
        
        break
    else:
        soma = int(soma)
        inverso = str(soma)[::-1]
        soma = soma + int(inverso)
        soma = str(soma)

print(soma)
    

#if soma == soma[::-1]:
#    print(soma)
#else:
#    print("não e palindrome")

