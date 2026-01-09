class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas
        

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def verificar_situacao(self):
        media = self.calcular_media()
        if media >= 7.0:
            return "Aprovado"
        else:
            return "Reprovado"
    
    def salvar_no_banco(self, conexao):
        cursor = conexao.cursor()

        sql = """
        INSERT INTO Alunos
        (nome, nota1, nota2, nota3, nota4, media, situacao)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        dados = (
            self.nome,
            self.notas[0],
            self.notas[1],
            self.notas[2],
            self.notas[3],
            self.calcular_media(),
            self.verificar_situacao()
        )

        cursor.execute(sql, dados)
        conexao.commit()
        cursor.close()