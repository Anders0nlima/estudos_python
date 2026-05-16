class Database:
    def __init__(self, conexao):
        self.conexao = conexao

    def salvar(self, ano_bissexto):
        cursor = self.conexao.cursor()

        sql = """
        INSERT INTO AnoBissexto (ano, resultado)
        VALUES (%s, %s)
        """

        dados = (
            ano_bissexto.ano,
            ano_bissexto.resultado
        )

        cursor.execute(sql, dados)
        self.conexao.commit()
        cursor.close()