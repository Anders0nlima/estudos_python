import random
joao = float(input('Digite o tamanho da lista: '))
pedro = float(input('Digite o tamanho da lista: '))

lista = []  
lista1 = []  

for i in range(int(joao)):
    numero = random.randint(1, 4)  
    lista.append(numero)  
     
soma = sum(lista)

for i in range(int(pedro)):
      
    numero = random.randint(1, 4)  
    lista1.append(numero)  
soma = sum(lista1)


# media = soma / tamanho
print(f' lista gerada {joao:".2f}")

# print(soma)
# print(media)
