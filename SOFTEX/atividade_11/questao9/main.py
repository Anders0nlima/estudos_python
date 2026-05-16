import mysql.connector
from bd import Database
from CategoriaNatacao import CategoriaNatacao

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin21',
    database='banco_exemplo'
)

ano_nascimento = int(input("Digite o ano de nascimento do atleta: "))

atleta = CategoriaNatacao(ano_nascimento)

print("--- Resultado ---")
print(f"Idade: {atleta.idade}")
print(f"Categoria: {atleta.categoria}")

banco = Database(conexao)
banco.salvar(atleta)

conexao.close()