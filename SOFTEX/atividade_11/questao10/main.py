import mysql.connector
from bd import Database
from LojaTintas import LojaTintas

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin21',
    database='banco_exemplo'
)

area = float(input("Digite a área a ser pintada (m²): "))

resultado = LojaTintas(area)

print("--- Resultado ---")
print(f"Litros necessários: {resultado.litros_necessarios:.2f}")
print(f"Latas a comprar: {resultado.latas}")
print(f"Preço total: R$ {resultado.preco_total:.2f}")

banco = Database(conexao)
banco.salvar(resultado)

conexao.close()