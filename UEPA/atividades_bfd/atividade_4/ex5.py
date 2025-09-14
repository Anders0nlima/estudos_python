lista_alunos = ["I", "II", "III", "IV", "V"]

prova_1 = [85, 80, 75, 85, 60]
prova_2 = [45, 70, 75, 35, 70]
prova_3 = [90, 70, 75, 35, 70]
prova_4 = [45, 75, 55, 90, 75]

notas = list(zip(prova_1, prova_2, prova_3, prova_4))

print(notas)


medias = []

for i, aluno in enumerate(lista_alunos):
    media = (sum(notas[i])/4)
    medias.append((aluno, media))

aluno_top, maior_media = max(medias)

print(f"medias finais: {medias}")
print(f"Aluno com maior nota final {aluno_top} com meida {maior_media}")

