import random 

matriz = [[round(random.uniform(1, 100), 2) for _ in range(10)] for _ in range(10)]

vetor_diagonal = [matriz[i][i] for i in range(10)]
print("matriz 10x10")
for linha in matriz:
    print(linha)

print("vetor da diadonal principal", vetor_diagonal)