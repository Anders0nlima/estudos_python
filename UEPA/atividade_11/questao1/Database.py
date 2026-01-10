class Database:
    def __init__(self, conexao):
        self.conexao = conexao

    def salvar(self, aluno):
        cursor = self.conexao.cursor()

        sql = """
        INSERT INTO Alunos
        (nome, nota1, nota2, nota3, nota4, media, situacao)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        dados = (
            aluno.nome,
            aluno.notas[0],
            aluno.notas[1],
            aluno.notas[2],
            aluno.notas[3],
            aluno.calcular_media(),
            aluno.verificar_situacao()
        )

        cursor.execute(sql, dados)
        self.conexao.commit()
        cursor.close()