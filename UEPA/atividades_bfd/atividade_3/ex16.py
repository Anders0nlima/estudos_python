lista_tempo = [20.90, 20.90, 20.50, 20.80, 20.60, 20.60, 20.90, 20.96]


tempo_ordem = sorted(lista_tempo)
valor_central1 = tempo_ordem[3]
valor_central2 = tempo_ordem[4]

print(valor_central1)
print(valor_central2)
mediana = ((valor_central1 + valor_central2)/2)

print(mediana)