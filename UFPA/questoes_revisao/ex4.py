lista_impares = []
lista_completa = []

for i in range(50):
    if i%2 != 0:
        lista_impares.append(i**2)

for j in range(50):
    lista_completa.append(j)
    
print(sum(lista_impares) - sum(lista_completa))
