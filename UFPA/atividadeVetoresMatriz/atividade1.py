vertor_original = []

print("Digite 10 valores inteiros e positivos:")

for i in range(10):
    valor = int(input(f"valor {i+1}: "))
    while valor <= 0:
        valor = int(input(f"valor{i+1} (positivo)"))
    vertor_original.append(valor)

vetor_mudado = []

for i in range(10):
    if i % 2 == 0:
        vetor_mudado.append(vertor_original[i]/2)
    else:
        vetor_mudado.append(vertor_original[i] * 3)

print("vetor original")
print(vertor_original)

print("vetor mudado")
print(vetor_mudado)