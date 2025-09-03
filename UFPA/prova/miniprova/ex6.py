matriz = []

for i in range(3):
    linha = []
    for j in range(3): 
        valor = int(input(f"Digite o valor da posição [{i}][{j}]: "))
        linha.append(valor) 
    matriz.append(linha)

print("Matriz 3x3:")
for linha in matriz:
    print(linha)

diagonal = [matriz[i][i] for i in range(3)]
print("\nDiagonal principal:", diagonal)

soma = sum(sum(linha) for linha in matriz)
print("Soma de todos os elementos:", soma)