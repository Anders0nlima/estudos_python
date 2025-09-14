num = input("digite um numero: ")
numInt = int(num)
print(num)

inverso = num[::-1]
resultadoinvertido = int(inverso)
print(inverso)


soma = numInt + resultadoinvertido


while (True):
    somaStr = str(soma)
    if somaStr == somaStr[::-1]: 
        break
    else:
        inversoSoma = int(str(soma)[::-1])
        soma = soma + inversoSoma

print(soma)


