lista_alunos = ["I", "II", "III", "IV", "V"]

prova_1 = [85, 80, 75, 85, 60]
prova_2 = [45, 70, 75, 35, 70]
prova_3 = [90, 70, 75, 35, 70]
prova_4 = [45, 75, 55, 90, 75]

notas = list(zip(prova_1, prova_2, prova_3, prova_4))

medias = []

notas = list(zip(prova_1, prova_2, prova_3, prova_4))

print(notas)


medias = []

for aluno, notas_aluno in zip(lista_alunos, notas):
    media = sum(notas_aluno)/len(notas_aluno)
    medias.append((aluno, media))

aluno_top, maior_media = max(medias, key = lambda x: x[1])

print(f"medias finais: {medias}")
print(f"Aluno com maior nota final {aluno_top} com meida {maior_media}")




""" 
aluno_top, maior_media = max(medias, key=lambda x: x[1])
Mas como cada item é uma tupla (("II", 73.75)), precisamos dizer ao Python por qual parte da tupla comparar.
Por padrão, ele compararia a primeira posição (o nome do aluno), mas queremos comparar a média (segundo valor). 
Por isso usamos:
key=lambda x: x[1]
Isso diz ao max:
“Compare os itens usando o segundo elemento da tupla (x[1])”.
"""