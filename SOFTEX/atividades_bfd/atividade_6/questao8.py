num = int(input("Digite um numero: "))

lista = []

for i in range(0, num, 2):
    quart = ((i+1)**2)
    lista.append(quart)

print(lista)