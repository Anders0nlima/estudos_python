#2. Contagem de Pares e Ímpares

from random import randint

tamanho = int(input("Quantos numeros vai ter na lista: "))
listaPar = []
listaImpar = []

for numero in range(tamanho):
    numero = (randint(1, 100))
    if numero % 2 == 0:
        listaPar.append(numero)
        quantP = len(listaPar)
    else:
        listaImpar.append(numero)
        quantI = len(listaImpar)


print(f"existem {quantP} numeros pares. Eles são: {listaPar}")
print(f"existem {quantI} numeros impares. Eles são: {listaImpar}")
    