def trocar_item(lista, valor1, valor2):
    if  valor1 in lista and valor2 in lista:
        index1 = lista.index(valor1)
        index2 = lista.index(valor2)
        
        lista[index1], lista[index2] = lista[index2], lista[index1]
        print(lista)
    else:
        print("o valor não esta na lista")

lista = [1, 2, 3, 4, 5]
print(lista)

print("Quais os dois valores voce quer trocar de posição")
valor1 = int(input("primeiro valor: "))
valor2 = int(input("segundo valor: "))


trocar_item(lista, valor1, valor2)