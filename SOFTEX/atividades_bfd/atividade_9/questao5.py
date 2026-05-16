def substituir_item(lista, num, novoValor):
    if num in lista:
        index = lista.index(num)
        lista[index] = novoValor
        print(lista)
    else:
        print("o valor não esta na lista")

lista = [1, 2, 3, 4, 5]
print(lista)

subst = int(input("digite um valor para substituir da lista: "))
novoValor = int(input("digite um novo valor para substituir da lista: "))


substituir_item(lista, subst, novoValor)