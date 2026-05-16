lista = []

def add_item(lista, num):
    lista.append(num)
    print(lista)

quantidade = int(input("digite quantos elemetos você quer na lista: "))

for i in range(quantidade):
    num = int(input("digite um valor para acicionar a lista: "))
    add_item(lista, num)