class Encapsulamento:
    def __init__(self): #privado por que tem dois underline
        self.__privado = "Variavel privada" #protegido, se nao tivesse o underline seria publico
        
    def metodo_publico(self):
        print(self.__privado)
        print(self.__metodo_privado())
        return "metodo_publico()"
    
    def __metodo_privado(self):
        return "__metodo_privado"
    

p = Encapsulamento()
#print(p.__privado)
#print(p.__metodo_privado())
print(p._Encapsulamento__metodo_privado())
print(p._Encapsulamento__privado)


print(p.metodo_publico())