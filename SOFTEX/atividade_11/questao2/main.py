from ParImpar import ParImpar
from Database import Database
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin21', #admin
    database='banco_exemplo'
)

numero_digitado = int(input("Digite um numero: "))

resultado = ParImpar(numero_digitado)

print("--- Resultado ---")
print(f"Classificação: {resultado.classificacao}")

banco = Database(conexao)
banco.salvar(resultado)

conexao.close()
