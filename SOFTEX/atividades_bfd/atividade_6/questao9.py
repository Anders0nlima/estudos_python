import random

tamanho = int(input("Qual o tamanho da lista: "))

lista = []

for i in range(tamanho):
    aleatorio = random.randint(1, 100)
    lista.append(aleatorio)

lista.sort()

print(lista)

if len(lista) % 2 == 0:
    meio_da_lista1 = len(lista) // 2
    meio_da_lista2 = (len(lista) // 2) - 1
    soma = lista[meio_da_lista1] + lista[meio_da_lista2]
    mediana = soma / 2
    print(mediana)
else:
    meio_da_lista = len(lista) // 2
    mediana = lista[meio_da_lista]
    print(mediana)
