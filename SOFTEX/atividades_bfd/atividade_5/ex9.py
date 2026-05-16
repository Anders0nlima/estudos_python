from random import randint

quant_alunos = int(input("Alunos na turma: "))

nomes_alunos = []
todas_notas = []

i = 0
while i < quant_alunos:
    nome = input("Nome do aluno: ")
    nomes_alunos.append(nome)

    notas_aluno = []
    j = 0
    while j < 4:        
        nota = randint(0, 10)
        notas_aluno.append(nota)
        j += 1

    todas_notas.append(notas_aluno)
    i += 1

medias = []
k = 0
while k < len(nomes_alunos):
    notas = todas_notas[k]
    media = sum(notas) / len(notas)
    medias.append(media)
    print(f"{nomes_alunos[k]}: notas {notas} | média: {media:.2f}")
    k += 1

if len(medias) > 0:
    media_geral = sum(medias) / len(medias)
else:
    media_geral = 0.0

print(f"\nMédia geral da turma: {media_geral:.2f}\n")

idx = 0
encontrados = 0
while idx < len(nomes_alunos):
    if medias[idx] > media_geral:
        print(f"{nomes_alunos[idx]} obteve média acima da média geral ({medias[idx]:.2f})")
        encontrados += 1
    idx += 1

if encontrados == 0:
    print("Nenhum aluno ficou acima da média geral.")



#mais facil com for
""" from random import randint
quant_alunos = int(input("alunos na turma: "))

todas_notas = []
nomes_alunos = []
cont1 = 0
while cont1 < quant_alunos:
    nome = input("Nome do aluno: ")
    nomes_alunos.append(nome)

    notas_aluno = []
    cont2 = 0
    while cont2 < 4:
        nota = randint(0, 10)
        notas_aluno.append(nota)
    todas_notas.append(notas_aluno)

medias = []
for nome, notas in zip(nomes_alunos, todas_notas):
    media = sum(notas)/len(notas)
    print(f"{nome}: notas {notas} | media: {media}")
    medias.append(media)

    media_geral = sum(medias)/len(medias)
    print(f"media geral {media_geral}")

    for nome, media in zip (nomes_alunos, medias):
        if media > media_geral:
            print(f"{nome} obteve maior madia geral") """
    
