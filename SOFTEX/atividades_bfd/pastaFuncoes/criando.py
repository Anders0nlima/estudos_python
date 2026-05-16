def mensagem():
    print("Boa tarde")


def mensagem():
    msg = "Boa tarde"
    return msg
    
def soma(a, b):
    resultado = a + b
    return resultado

print(mensagem(), soma(1, 2))

numero = int(input("Qual numero? "))

def quadrado(num):
    aoQradrado = num**2
    return aoQradrado

print(quadrado(numero))

# sem return
def dados(n, p):
    print(f"seu nome é {n} e você tem {p} anos")
     

nome = input("Qual sua nome: ")
idade = int(input("Qual sua idade: "))
dados(nome, idade)


# sem return
def dados(n, p):
    msg = (f"seu nome é {n} e você tem {p} anos")
    return msg 

nome = input("Qual sua nome: ")
idade = int(input("Qual sua idade: "))
print(dados(nome, idade))


#nome e curso
def info(n, c):
    msg = (f"Ola {n}, seja bem-vindo ao curso {c}")
    return msg

nome = input("Qual é o seu nome: ")
curso = input("Qual o seu curso: ")

print(info(nome, curso))


        