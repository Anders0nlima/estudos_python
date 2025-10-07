#4. Banco de Nomes (filtros com for e if)

tamanho = int(input("Quantos nomes quer por: ")) # olhar isso depois como nao utilizar isso

listaNomes = []
listaAchado = []

for nome in range(tamanho):
    nomes = input("Digite um nome: ").lower()
    listaNomes.append(nomes)

print(listaNomes)

letra = input("Digite uma letra: ")

for name in listaNomes:
    if name.startswith(letra):
        listaAchado.append(name)

if listaAchado:
    print(listaAchado)
else:
    print("nao encontrado")
   
