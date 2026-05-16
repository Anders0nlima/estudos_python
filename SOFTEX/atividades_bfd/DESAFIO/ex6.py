tamanho = int(input("quantas pessas há na lista: "))

lista = []

for i in range(tamanho):
    nomes = input("Digite o nome: ")
    listaNomes = lista.append(nomes)

lista.sort()

print(lista)
