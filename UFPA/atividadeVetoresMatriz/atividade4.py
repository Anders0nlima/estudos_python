import random 

matriz = [[random.randint(1, 20) for _ in range(5)] for _ in range(5)]

n = 5

diagonal_sec = [matriz[i][n-1-i] for i in range(n)]
soma_diag = sum(diagonal_sec)

print("Matriz 5x5")
for linha in matriz:
    print(linha)


print("diagonal segundaria: ", diagonal_sec)
print("Soma da diagonal secundaria: ", soma_diag)