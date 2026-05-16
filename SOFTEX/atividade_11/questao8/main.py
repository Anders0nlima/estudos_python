import mysql.connector
from bd import Database
from Emprestimo import Emprestimo

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin21',
    database='banco_exemplo'
)

valor_casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o salário: R$ "))
anos = int(input("Em quantos anos vai pagar: "))

resultado = Emprestimo(valor_casa, salario, anos)

print("--- Resultado ---")
print(f"Prestação mensal: R$ {resultado.prestacao_mensal:.2f}")
print(resultado.resultado)

banco = Database(conexao)
banco.salvar(resultado)

conexao.close()