votos = ['A', 'B', 'A', 'C', 'C', 'C', 'A', 'C', 'C', 'B', 'A']


votos_produtos = {}

for voto in votos:
    if voto in votos_produtos:
        votos_produtos[voto] += 1
    else:
        votos_produtos[voto] = 1

print(votos_produtos)


mais_votado = max(votos_produtos, key=votos_produtos.get)
print("Produto mais votado:", mais_votado)