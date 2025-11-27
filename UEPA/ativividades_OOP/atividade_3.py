banco_dados = {}

def numero_conta():
    import random
    return random.randint(1, 100)

def salva_banco(conta):
    numero = numero_conta()
    banco_dados[numero] = {"titular": conta.titulo, "tipo": conta.tipo, "saldo": conta.saldo}

def listar_contas():
    for numero, dados in banco_dados.items():
        print(f"Conta {numero} | Titular: {dados['titular']} | Tipo: {dados['tipo']} | Saldo: R$ {dados['saldo']:.2f}")



class ContaBancaria():
    def __init__(self, tipo, titular):
        self.tipo = tipo
        self.titulo = titular
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor 
            print(f"valor depositado: {valor:.2f}")
        else:
            print("nao pode valor negativo")
        
    def sacar(self, valor):
        if valor <= 0:
            print("nao pode sacar valores negativo ou nada")
        elif valor > self.saldo:
            print("valor ultrapassa seu saldo")
        else:
            self.saldo -= valor
            print(f"valor sacado: {valor:.2f}") 
        
    def extrato(self):
            print(f"O titular {self.titulo}, do tipo {self.tipo}, possui atualmente {self.saldo:.2f}")


tipo = input("Qual o tipo de conta? ")
titular = input("Qual o seu nome? ")

conta = ContaBancaria(tipo, titular)

while True:
    print("""
Serviços:
1- Deposito
2- Saque
3- Extrato
4- Salvar 
5- Ver Dados
6- Sair
""")
    opcao = int(input("Serviço: "))

    if opcao == 1:
        valor = float(input("Deposito: "))
        conta.depositar(valor)
    
    elif opcao == 2:
        valor = float(input("saque: "))
        conta.sacar(valor)
    
    elif opcao == 3:
        conta.extrato()
    
    elif opcao == 4:
        salva_banco(conta)
    
    elif opcao == 5:
        listar_contas()
    
    elif opcao == 6:
        print("saindo...")
        break

    else:
        print("Opcoo invalida")