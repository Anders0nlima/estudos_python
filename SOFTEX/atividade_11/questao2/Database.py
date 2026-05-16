class Database:
    def __init__(self, conexao):
        self.conexao = conexao
    
    def salvar(self, par_impar):
        cursor = self.conexao.cursor()

        sql = """
        INSERT INTO ParImpar
        (numero, classificacao)
        VALUES (%s, %s)
        """

        dados = (
            par_impar.numero,
            par_impar.classificacao
        )

        cursor.execute(sql, dados)
        self.conexao.commit()
        cursor.close()
