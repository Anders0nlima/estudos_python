#calculadora 
print("1- Soma")
print("2- Subtração")
print("3- Multiplicação")
print("4- Divisão")

ope = int(input("Qual operção deseja fazer: "))

num1 = int(input("Informe o primeiro valor: "))
num2 = int(input("Informe o segundo valor: ")) # nao pode ser zero na função nda divisão


def soma(p, s):
    return (p + s)

def subtracao(p, s):
    return (p - s)

def multi(p, s):
    return (p * s)

def divisao(p, s):
    if s == 0:
        return "Divisão noa pode ser por 0"
    return (p / s)

if ope == 1: 
  operacao = "Soma"
  resultado = soma(num1, num2)

elif ope == 2: 
  operacao = "Subtração"
  resultado = subtracao(num1, num2)
    
elif ope == 3: 
  operacao = "Multiplicação"
  resultado = multi(num1, num2)

elif ope == 4: 
  operacao = "Divisão"
  resultado = divisao(num1, num2)
        
else:
    print("Operção não encontrada, valor valido entre [1 - 4]")
    
    
# essa estrutura de if e else poderia ser substituida som o uso de match e case 
# match opcao:
#   case 1:
#     print(soma)  
    

print(f"O resultado da {operacao} é: {resultado}")


# msg = """
# nao precisa 
# de print
# um de baixo 
# do outro
# """