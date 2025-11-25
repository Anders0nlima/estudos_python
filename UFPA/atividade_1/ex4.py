soma_quadrados = 0
for i in range(1, 11):
    soma_quadrados += i**2


lista = []
for j in range(1, 11):
    lista.append(j)

soma_naturais = (sum(lista)**2)


diferenca = (soma_naturais - soma_quadrados)

print(diferenca)