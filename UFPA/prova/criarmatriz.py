import random

cont = 0

matriz = [[random.randint(1, 100) for _ in range(4)] for _ in range(4)]

for i in range(4):
    for j in range(4):
        if matriz[i][j] % 2 == 0:
            cont += 1


print(matriz)

print(cont)