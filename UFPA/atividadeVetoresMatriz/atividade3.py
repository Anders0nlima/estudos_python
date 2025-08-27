A = [[1, 2, 3], [4, 5, 6]]
B = [[6, 7, 8], [9, 10, 11]]

C = [[A[i][j] + B[i][j] for j in range(3)] for i in range(2)]

print("Matriz A: ", A)
print("Matriz B: ", B)
print("Soma: ", C)

