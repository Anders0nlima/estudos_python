import mysql.connector
from bd import Database
from Reajuste import Reajuste

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin21',
    database='banco_exemplo'
)

salario = float(input("Digite o salário do funcionário: R$ "))

reajuste = Reajuste(salario)

print("--- Resultado ---")
print(f"Salário original: R$ {reajuste.salario_original:.2f}")
print(f"Percentual de aumento: {reajuste.percentual}%")
print(f"Valor do aumento: R$ {reajuste.valor_aumento:.2f}")
print(f"Salário final: R$ {reajuste.salario_final:.2f}")

banco = Database(conexao)
banco.salvar(reajuste)

conexao.close()