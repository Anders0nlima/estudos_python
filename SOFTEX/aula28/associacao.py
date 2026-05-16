class Aluno:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.__material = None
    
    @property
    def material(self):
        return self.__material
    
    @material.setter
    def material(self, material):
        self.__material = material


class MaterialEscola:
    def __init__(self, nome_material):
        self.nome_material = nome_material
        
    def usar_material(self):
        return f"{self.nome_material} está sendo usado"
    

aluno = Aluno("Bruno")
caderno = MaterialEscola("Caderno")
lapis = MaterialEscola("Lapis")

#associação
aluno.material = caderno
aluno.material = lapis


print(caderno.usar_material())
print(aluno.material.usar_material())