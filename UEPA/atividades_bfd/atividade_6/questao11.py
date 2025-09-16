tamanho_nomes = int(input("quantos nomes você quer que a lista tenha: "))

banco_de_nomes = []

for i in range(tamanho_nomes):
    nomes = input("digite o nome: ").upper()
    banco_de_nomes.append(nomes)

print(banco_de_nomes)

primeira_letra = []
for nomes in banco_de_nomes:
    primeira_letra.append(nomes[0])

print(primeira_letra)


pesquisa_nome = input("Qual a inicial do nome desejado: ").upper()

for nome in banco_de_nomes:
    if nome[0] == pesquisa_nome:
        print(nome)



