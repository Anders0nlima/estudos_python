lista = []

for i in range(5):
  num = int(input("Numero: "))
  lista.append(num)

maior = max(lista)
menor = min(lista)


print(f"lista: {lista}")
print(f"maior numero: {maior}")
print(f"menor numero: {menor}")