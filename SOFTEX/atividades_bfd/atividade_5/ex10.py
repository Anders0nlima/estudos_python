
quant_nomes = int(input("Quanto nomes há na bando de dados: "))

lista_nomes = []
cont1 = 0
while cont1 < quant_nomes:
    nome = input("Adicionar nome: ").lower()
    lista_nomes.append(nome)
    cont1 += 1

print(lista_nomes)

print("=== Procurar alguem ===")

inicial = input("Qual a inicial do nome: ").lower()
lista_achada = []
for nome in lista_nomes:
    if nome.startswith(inicial):
        lista_achada.append(nome)

print(lista_achada)
