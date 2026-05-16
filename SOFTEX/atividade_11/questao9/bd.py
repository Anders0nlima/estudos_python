class Database:
    def __init__(self, conexao):
        self.conexao = conexao

    def salvar(self, atleta):
        cursor = self.conexao.cursor()

        sql = """
        INSERT INTO NatacaoCategoria (ano_nascimento, idade, categoria)
        VALUES (%s, %s, %s)
        """

        dados = (
            atleta.ano_nascimento,
            atleta.idade,
            atleta.categoria
        )

        cursor.execute(sql, dados)
        self.conexao.commit()
        cursor.close()