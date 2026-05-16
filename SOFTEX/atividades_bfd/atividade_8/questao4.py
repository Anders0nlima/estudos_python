nome = input("Qual o seu nome: ")
idade = int(input("Quantos anos você tem: "))
altura = float(input("Qual sua altura: "))

def info(nome, idade, altura):
    return (f"{nome} tem {idade} anos e uma altura de {altura} metros")

print(info(nome, idade, altura))