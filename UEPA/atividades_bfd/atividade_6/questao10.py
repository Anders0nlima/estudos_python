import random

quant_alunos = int(input("Quantos alunos há na sala: "))

lista_nomes = []
lista_notas = []

for i in range(quant_alunos):
    nome = input("nome do aluno: ")
    lista_nomes.append(nome)

    notas_aleatorias = random.randint(0, 10)
    lista_notas.append(notas_aleatorias)

media_notas = sum(lista_notas)/len(lista_notas)
print(f'{media_notas:.2f}')

acima_media = []

for i in range(quant_alunos):
    if lista_notas[i] > media_notas:
       acima_media.append(lista_nomes[i])

print(f"\nTotal de alunos acima da média: {len(acima_media)}")
print("Alunos acima da média:", acima_media)

for nome, nota in zip(lista_nomes, lista_nomes):
    print(f"{nome} : {nota}")
