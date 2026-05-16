import mysql.connector #importei a biblioteca

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin',
    database = 'escola_x'
)

#cursor = conexao.cursor()

#cursor.execute(
#    f'INSERT INTO alunos (id, nome, idade, altura)'
#    'VALUES (16, "Sofia", 16, 1.80)'
#)


#conexao.commit()
#cursor.close()
conexao.close()