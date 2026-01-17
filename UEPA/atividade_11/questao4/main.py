import mysql.connector
from bd import Database
from TrianguloValido import TrianguloValido

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin21', #admin
    database='banco_exemplo'
)

lados = []
for i in range(3):
    lado = int(input(f"Digite o lado {i + 1}: "))
    lados.append(lado)

triangulo = TrianguloValido(lados[0], lados[1], lados[2])

print("--- Resultado ---")
print(f"{triangulo.tipo}")


banco = Database(conexao)
banco.salvar(triangulo)

conexao.close()