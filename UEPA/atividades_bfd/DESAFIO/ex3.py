import random
tamanho = int(input('Digite o tamanho da lista: '))
lista = []  
for i in range(tamanho):
    numero = random.randint(1, 100)  
    lista.append(numero)  
soma = sum(lista)
media = soma / tamanho
print("Lista gerada:", lista)
print(soma)
print(media)
