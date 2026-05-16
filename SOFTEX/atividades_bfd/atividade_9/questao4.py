def remover_item(lista, num):
    if num in lista:
        lista.remove(num)
        print(lista)
    else:
        print("o valor não esta na lista")

lista = [1, 2, 3, 4, 5]
print(lista)

remover = int(input("digite um valor para remover da lista: "))


remover_item(lista, remover)