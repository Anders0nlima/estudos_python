lista = [1, 2, 3, 4, 5]

#backup da lista
def backup_item(lista):
    backup = lista.copy()
    print("backup: ", backup)

backup_item(lista)

#remover um valor
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

#adicionar um valor
num = int(input("digite um valor para acicionar a lista: "))

def add_item(lista, num):
    lista.append(num)
    print(lista)

add_item(lista, num)

