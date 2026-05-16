import mysql.connector
from bd import Database
from IMC import IMC

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin21',
    database='banco_exemplo'
)

peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))

resultado = IMC(peso, altura)

print("--- Resultado ---")
print(f"IMC: {resultado.imc:.2f}")
print(f"Categoria: {resultado.categoria}")

banco = Database(conexao)
banco.salvar(resultado)

conexao.close()