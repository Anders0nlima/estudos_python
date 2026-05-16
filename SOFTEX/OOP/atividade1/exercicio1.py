class Dog():
    def __init__(self, nome):
        self.nome = nome
    
    def sentar(self):
        print(f"senta {self.nome}")

    def deita(self):
        print(f"deita {self.nome}")
    
    def fica(self):
        print(f"fica {self.nome}")
    
    def vem(self):
        print(f"vem {self.nome}")
    
    def junto(self):
        print(f"senta {self.nome}")
        print(f"deita {self.nome}")
        print(f"fica {self.nome}")
        print(f"vem {self.nome}")


dog_nome = input("Qual o nome do cachoroo? ")
dog = Dog(dog_nome)

while True:
    print("""
        Escolha uma opção:
        1- Sentar 
        2- Deitar
        3- Ficar 
        4- Vem
        5- Junto
        0- sair
    """)
    
    opcao = int(input("escolha uma opção da tebla: "))


    acoes = {
        1: dog.sentar,
        2: dog.deita,
        3: dog.fica,
        4: dog.vem,
        5: dog.junto
    }
    if opcao == 0:
        print("Saindo...")
        break

    acao = acoes.get(opcao)

    if acao:
        acao()
    else:
        print("O cachorro não sabe fazer essa opção :(")
