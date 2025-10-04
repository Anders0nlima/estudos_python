votos = ['A', 'B', 'A', 'C', 'C', 'C', 'A', 'C', 'C', 'B', 'A']

votos_prudutos = {}

for voto in votos:
    if voto in votos_prudutos:
        votos_prudutos[voto] += 1
    else:
        votos_prudutos[voto] = 1

print(votos_prudutos)


mais_votado = max(votos_prudutos, key=votos_prudutos.get)
print("Produto mais votado:", mais_votado)