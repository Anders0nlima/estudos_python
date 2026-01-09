from Aluno import Aluno
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='banco_exemplo'
)

nome = input("Digite o nome do aluno: ")

notas = []
for i in range(4):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

aluno = Aluno(nome, notas)


print("--- Resultado ---")
print(f"Média: {aluno.calcular_media():.2f}")
print(f"Situação: {aluno.verificar_situacao()}")

aluno.salvar_no_banco(conexao)

conexao.close()