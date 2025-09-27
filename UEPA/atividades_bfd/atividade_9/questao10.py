def add_item(lista, num):
    lista.append(num)
    print(lista)

def remover_item(lista, num):
    if num in lista:
        lista.remove(num)
        print(lista)
    else:
        print("o valor não esta na lista")
        
def substituir_item(lista, num, novoValor):
    if num in lista:
        index = lista.index(num)
        lista[index] = novoValor
        print(lista)
    else:
        print("o valor não esta na lista")
        
def trocar_item(lista, valor1, valor2):
    if  valor1 in lista and valor2 in lista:
        index1 = lista.index(valor1)
        index2 = lista.index(valor2)
        
        lista[index1], lista[index2] = lista[index2], lista[index1]
        print(lista)
    else:
        print("o valor não esta na lista")

lista = []

print("Crie sua lista: ")

def add_itens(lista, num):
    lista.append(num)
    print(lista)

quantidade = int(input("digite quantos elemetos você quer na lista: "))

for i in range(quantidade):
    num = int(input("digite um valor para acicionar a lista: "))
    add_itens(lista, num)

print(f"O que voce quer fazer com a lista: {lista}")
quadro = """
1- Adicionar item na lista
2- Remover item da lista
3- substituir item da lista
4- trocar item da lista
"""
print(quadro)


escolha = int(input("Digite sua escolha: "))

match escolha:
    case 1:
        num = int(input("digite um valor para acicionar a lista:"))
        add_item(lista, num)
    case 2:
        num = int(input("Digite o valor que deseja remover da lista: "))
        remover_item(lista, num)
    case 3:
        antigo = int(input("Digite o valor que deseja substituir: "))
        novo = int(input("Digite o novo valor: "))
        substituir_item(lista, antigo, novo)
    case 4:
        i1 = int(input("Digite o índice do primeiro item: "))
        i2 = int(input("Digite o índice do segundo item: "))
        trocar_item(lista, i1, i2)
    case _:
        print("Opção inválida.")

   
        
