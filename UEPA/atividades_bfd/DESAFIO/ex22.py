num = input("Digite um numero: ")

numInt = int(num)
print(numInt)


invertido = num[::-1]
numInvertido = int(invertido)
print(numInvertido)

soma = numInt + numInvertido


while(True):
    somaStr = str(soma)
    if somaStr == somaStr[::-1]:
        break
    else:
        invertido = int(somaStr[::-1])
        soma = soma + invertido

print(soma)

