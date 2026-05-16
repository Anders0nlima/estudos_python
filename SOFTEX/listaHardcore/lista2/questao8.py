#8. Média e Desempenho de Alunos

aluno = {}
listaNotas = []

print("Sistema Escolar")
nome = input("Nome do aluno: ")
aluno["nome"] = nome
for i in range(3):
    notas = float(input(f"{i+1}-Nota: "))
    listaNotas.append(notas)
    aluno["notas"]  = listaNotas

media = sum(listaNotas)/len(listaNotas)
aluno["media"] = media

if media >= 7:
    print("aprovado")
else:
    print("reprovado")

print(aluno)    
