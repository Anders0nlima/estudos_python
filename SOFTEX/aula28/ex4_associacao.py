class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.__ferramenta = None
    
    @property
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Ferramenta:
    def __init__(self, nome_ferramenta):
        self.nome_ferramenta = nome_ferramenta
        
    def usar_ferramenta(self):
        return f"{self.nome_ferramenta} está sendo usado"
    

escritor = Escritor("Anderson")
computador = Ferramenta("computador")

#associação
escritor.material = computador


print(computador.usar_ferramenta())
print(escritor.material.usar_ferramenta())