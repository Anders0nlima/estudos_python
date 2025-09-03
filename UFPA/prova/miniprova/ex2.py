op = int(input("codigo: "))

lista_notas = []

while op != -1:
    notas = int(input("digite sua nota: "))
    op = int(input("codigo: "))
    lista_notas.append(notas)

print("O programa acabou")
soma = sum(lista_notas)
media = soma/len(lista_notas)
print(f"Media das notas: {media}")