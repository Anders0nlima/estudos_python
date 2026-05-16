#1. Quadrados Perfeitos Aleatórios (random + math)


from random import randint
from math import sqrt

lista = []
listaPerfeito = []

quant = int(input("quantos numeros quer sotear: "))

for numero in range(quant):
    numero = (randint(1, 100))
    lista.append(numero)

    if (sqrt(numero)).is_integer():
        listaPerfeito.append(numero)


print("Lista geral: ", lista)
print("Lista dos quadrados perfeitos: ", listaPerfeito)
