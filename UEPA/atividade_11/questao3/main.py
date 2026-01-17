import mysql.connector
from DataBase import Database
from MaiorIdade import MaiorIdade

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin21', #admin
    database='banco_exemplo'
)

idade_digitada = int(input("Qual sua idade: "))

resultado = MaiorIdade(idade_digitada)
print("--- Resultado ---")
print(f"ACESSO: {resultado.acesso}")

banco = Database(conexao)
banco.salva(resultado)

conexao.close()
