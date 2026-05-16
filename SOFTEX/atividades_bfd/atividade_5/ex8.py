import random 

tamanho = int(input("tamanho da lista: "))

num = []

i = 0

while i < tamanho:
    num.append(random.randint(1, 100))
    i += 1

print("Numeros gerados: ")
print(num)


pares = []
impar = []
j = 0

while j < len(num):
    if num[j] % 2 == 0:
       pares.append(num[j])
    else:
        impar.append(num[j])
    j += 1

print("Numeros pares gerados:")
print(pares)
print("Numeros pares gerados:")
print(impar)

tamanho_par = len(pares)
tamanho_impar = len(impar)

print(f"a quantidade de numeros gerados na lista par é: {tamanho_par}")
print(f"a quantidade de numeros gerados na lista impar é: {tamanho_impar}")

