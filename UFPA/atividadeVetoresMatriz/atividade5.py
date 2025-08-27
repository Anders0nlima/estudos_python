import random

matriz = [[random.randint(1,20) for _ in range(4)] for _ in range(4)]

cont = sum(1 for i in range(4) for j in range(4) if matriz[i][j] > 10)

print("Matriz 4*4: ")
for linha in matriz:
    print(linha)

print("quantidade de valores > 10: ", cont )