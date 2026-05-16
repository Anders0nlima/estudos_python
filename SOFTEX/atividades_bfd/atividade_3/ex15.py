lista_alunos = ["X", "Y", "Z"]

lista_notas = [[5, 5, 5, 10, 6], [4, 9, 3, 9, 5], [5, 5, 8, 5, 6]] 

for i in range(len(lista_alunos)):
    nome = lista_alunos[i]
    notas = lista_notas[i]
    media = sum(notas) / len(notas)
    if(media >= 6):
        print(f"Média do aluno {nome}: {media} (aprovado)")
    else:
        print(f"Média do aluno {nome}: {media} (reprovado)")