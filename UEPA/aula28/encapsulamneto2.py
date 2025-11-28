class Encapsulamento:
    def __init__(self):
        self.__privado = "Variavel privada" 
        self._protegido = "Variavel protegida" 

    def metodo_publico(self):
        print(self.__privado) 
        print(self.__metodo_privado()) 

    def __metodo_privado(self):
        return "Valor do método privado"

p = Encapsulamento()
p.metodo_publico() 


print(p._Encapsulamento__metodo_privado())
print(p._Encapsulamento__privado)