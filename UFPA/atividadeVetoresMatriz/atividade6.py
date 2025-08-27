import random

matriz = [[random.randint(1, 9) for _ in range(5)] for _ in range(5)]


print("matriz")

for linha in matriz:
    print(linha)


print("Soma por linha")
for i in range(5):
    soma = sum(matriz[i])
    print(f"linha {i+1}: soma = {soma} : {"par" if soma % 2 == 0  else "impar"}")

print("Soma por coluna:")
for j in range(5):
    soma = sum(matriz[i][j] for i in range(5))
    print(f"coluna {j+1}: soma = {soma} : {"par" if soma % 2 == 2 else "impar"}")
