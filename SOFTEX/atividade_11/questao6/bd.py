class Database:
    def __init__(self, conexao):
        self.conexao = conexao

    def salvar(self, imc):
        cursor = self.conexao.cursor()

        sql = """
        INSERT INTO IMC (peso, altura, imc, categoria)
        VALUES (%s, %s, %s, %s)
        """

        dados = (
            imc.peso,
            imc.altura,
            imc.imc,
            imc.categoria
        )

        cursor.execute(sql, dados)
        self.conexao.commit()
        cursor.close()