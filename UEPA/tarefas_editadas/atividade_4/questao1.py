import random 
cont = 0
impar = 0
par = 0

escolha = input("escolha entre impar ou par:")


while cont <= 2:
    comp = random.randint(0, 10)

    seu_dado = int(input("Numero: "))

    soma = comp + seu_dado
    if soma % 2 == 0:
        par += 1
    else:
        impar += 1

    print(soma)
    
    cont += 1

print("Fim de jogo")
print("numeros impares: ", impar)
print("numeros pares: ", par)

if par > impar:
    if escolha == "PAR":
        print("Você ganhou")
    else: 
        print("Você perdeu")
else:
    if escolha == "IMPAR":
        print("Você ganhou")
    else:
        print("Você perdeu")