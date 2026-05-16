listaNomes = []
listaTamanhos = []
cont = 0


while cont < 3: 
    palavras = input("Digite palavras: ")
    listaNomes.append(palavras)
    tamanho = len(listaNomes[cont])
    cont = cont + 1 
tamanho.sort()
print(tamanho)
    