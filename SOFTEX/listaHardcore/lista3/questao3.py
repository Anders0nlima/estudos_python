#Notas de Alunos – Vários Registros  ==== cancelar
quant = int(input("Quantos alunos há na clase: "))
alunos = []


# Notas de Alunos – Vários Registros

quant = int(input("Quantos alunos há na classe: "))
alunos = []  # lista para guardar todos os alunos

for i in range(quant):
    nome = input(f"Nome do aluno {i+1}: ")
    notas = []  # lista de notas do aluno atual

    for j in range(3):
        nota = float(input(f"Nota {j+1} de {nome}: "))
        notas.append(nota)

    aluno = {          # cria o dicionário do aluno
        "nome": nome,
        "notas": notas
    }

    alunos.append(aluno)  # adiciona o dicionário na lista geral

# Exibe os dados
print("\n=== Dados dos Alunos ===")
for aluno in alunos:
    media = sum(aluno["notas"]) / len(aluno["notas"])
    print(f"Aluno: {aluno['nome']} - Notas: {aluno['notas']} - Média: {media:.2f}")

