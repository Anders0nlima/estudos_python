lista = [1, 2, 3, 4, 5]
print(lista)
num = int(input("digite um valor para acicionar a lista: "))

def add_item(lista, num):
    lista.append(num)
    print(lista)


add_item(lista, num)