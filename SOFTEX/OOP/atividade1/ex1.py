class Cachorro():
    altura_cachorro = None

    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade
    
    def Latir(self):
        return (f"{self.nome} está latindo")


c1 = Cachorro("Rex", "pastor-alemao", 10)
c1.altura_cachorro = 30
print(f"O nome do cachorro é {c1.nome}, sua raça: {c1.raca}, sua idade: {c1.idade}, e sua altura é {c1.altura_cachorro} cm")


c2 = Cachorro("Thor", "bulldog", 13)
print(c2.Latir())