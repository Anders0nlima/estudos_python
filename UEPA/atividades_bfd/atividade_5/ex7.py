import random 
import math

tamanho = int(input("tamanho da lista: "))

num = []

i = 0

while i < tamanho:
    num.append(random.randint(1, 100))
    i += 1
    
print("Numeros gerados: ")
print(num)


quand_perfeito = []

j = 0

while j < len(num):
    numero = num[j]
    raiz = math.sqrt(numero)
    
    if raiz == int(raiz):
      quand_perfeito.append(numero)
    
    j += 1

print("quadrados perfeitos: ")
print(quand_perfeito)
