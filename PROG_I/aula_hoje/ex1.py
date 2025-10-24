lista = []

for i in range(4):
    notas = int(input("Temperatura: "))
    lista.append(notas)
print(lista)

media = sum(lista)/len(lista)
print(media)