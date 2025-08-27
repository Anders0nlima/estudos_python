import random

vetor1 = [random.randint(1,100) for _ in range(10)]
vetor2 = [random.randint(1,100) for _ in range(10)]


vetor_difereca = [vetor1[i] - vetor2[i] for i in range(10)]
vetor_soma = [vetor1[i] + vetor2[i] for i in range(10)]
vetor_multiplicacao = [vetor1[i] * vetor2[i] for i in range(10)]


print("vetor 1: ", vetor1)
print("vetor 2: ", vetor2)
print(f"diferença ente o {vetor1} e o {vetor2}: ", vetor_difereca)
print(f"soma entre o {vetor1} e o {vetor2}: ", vetor_soma)
print(f"multiplicação entre o {vetor1} e o {vetor2}: ", vetor_multiplicacao)
