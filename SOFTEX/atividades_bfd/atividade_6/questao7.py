num = int(input("Digite um numero: "))

lista = []

for i in range(0, num, 1):
    quart = ((i+1)**2)
    lista.append(quart)

print(lista)