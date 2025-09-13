import random

tamanho = int(input("Digite a quantidade de notas: "))

lista = []

for i in range(tamanho):
    numero = random.randint(1, 10)
    lista.append(numero)

soma = sum(lista)

media = soma/tamanho

print(lista)
print(media)
    