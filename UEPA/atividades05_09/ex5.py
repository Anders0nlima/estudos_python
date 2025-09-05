cont = 0
lista = []

while cont <= 9:
    print(cont)
    cont += 1
    lista.append(cont)

soma = sum(lista)
print(lista)
print(f"A soma dos numeros são: {soma}")