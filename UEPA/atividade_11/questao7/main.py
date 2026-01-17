import mysql.connector
from bd import Database
from AnoBissexto import AnoBissexto

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin21',
    database='banco_exemplo'
)

ano = int(input("Digite um ano: "))

resultado = AnoBissexto(ano)

print("--- Resultado ---")
print(resultado.resultado)

banco = Database(conexao)
banco.salvar(resultado)

conexao.close()