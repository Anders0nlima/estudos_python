class Mochila:
    def __init__(self):
        self._materiais = []
        
    
    def inserir_materiais(self, *materiais):
        self._materiais += materiais
    
    def lista_materiais(self):
        for material in self._materiais:
            print(material.nome, material.peso)
            
    def total_peso_mochila(self):
        peso = sum([p.peso for p in self._materiais])
        return peso

class Materiais:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        
mochila = Mochila()
n1 = Materiais("caderno", 0.25)
n2 = Materiais("livro", 0.55)

mochila.inserir_materiais(n1, n2)
mochila.lista_materiais()
print(mochila.total_peso_mochila())
    