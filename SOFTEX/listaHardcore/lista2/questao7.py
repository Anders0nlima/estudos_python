#7. Pesquisa de Produtos (listas + dicionários)


votos = ['A', 'B', 'A', 'C', 'C', 'C', 'A', 'C', 'C', 'B', 'A']

contA = 0
contB = 0
contC = 0

for i in range(len(votos)):
    if votos[i] == "A":
        contA += 1
    elif votos[i] == "B":
        contB += 1
    else:
        contC += 1
    
print(f"A: {contA}, B: {contB}, C: {contC}")