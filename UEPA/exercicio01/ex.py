# 1- Conversão de Tipos
tipoA = "123"
tipoB = int(tipoA)
tipoC = float(tipoA)

print(tipoB)
print(tipoC)


# 2- Operações com Strings
tipoD = "Python e incrivel!"

quantCara = len(tipoD)
maius = tipoD.upper()
troca = tipoD.replace("incrivel",  "poderoso")

print(quantCara)
print(maius)
print(troca)


# 3- Listas e Indexação
numeros = [10, 20, 30, 40, 50]

print(numeros[2])
numeros.append(60)
numeros.remove(20)

print(numeros) 


# 4- Dicionários
aluno = {
    "aluno" : "Maria", 
    "idade" : 22, 
    "curso" : "Engenharia"
}

aluno["notas"] = [8.5, 7.0, 9.2]

print(aluno["curso"])


# 5- Tuplas e Conjuntos
cores = ("vermelho", "verde", "azul", "verde")

novo_cores = set(cores)
novo_cores.add("amarelo")

print(novo_cores)


# 6- Operações Matemáticas
a = 15 
b = 4 

divisao = a // b
resto = a % b

print(divisao)
print(resto)


# 7- Verificação de Tipos
dados = [42, 3.14, "Python", True, [1, 2]]

for item in dados:
    print(type(item))


# 8- Manipulação de Strings
tipoE = "programação"

reverso = "".join(reversed(tipoE))
isbool = tipoE == reverso
print(isbool)
print(reverso)


# 9- Listas Aninhadas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matriz[1][1])

matriz[2][1] = 10

print(matriz)


# 10- Desafio Final
estoque = {
"maca": 10,
"banana": 5,
"laranja": 8
}

estoque.update({"pera": 12})
del estoque["banana"]

print(estoque.keys())


