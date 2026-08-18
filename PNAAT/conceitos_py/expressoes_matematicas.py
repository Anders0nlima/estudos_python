# parte 3

# Expressões Matemáticas
# Usando parênteses para controlar a ordem de avaliação

# Definindo variáveis
a = 5
b = 3
c = 2
d = 10

# Expressão com operadores matemáticos
expressao_matematica = (a + b) * (c - d) / (a ** c)
print(f"Expressão Matemática: {expressao_matematica}") 

# Equação grande
equacao_grande = ((a + b) * (c - d) / (a ** c)) + (d / (a + c) - b * c)
print(f"Equação Grande: {equacao_grande}") 

# Expressões Condicionais Complexas
# Combinando operadores lógicos e de comparação

# Definindo variáveis
x = 8
y = 12
z = 20

# Expressão complexa com operadores condicionais
expressao_condicional = (x > y and y < z) or (x + y > z and not (z == x * 2))
print(f"Expressão Condicional: {expressao_condicional}") 

# Outra expressão complexa
outra_expressao_condicional = (x < y and y == z) or (x + z > y and not (x == z / 2))
print(f"Outra Expressão Condicional: {outra_expressao_condicional}") 

# Expressões Relacionais Complexas
# Combinando operadores matemáticos, lógicos e de comparação

# Definindo variáveis
m = 15
n = 25
p = 35

# Expressão complexa combinando diferentes operadores
expressao_relacional = ((m * n) > (p + m)) and ((p / n) < m) or not (p == m + n)
print(f"Expressão Relacional: {expressao_relacional}") 

# Outra expressão relacional complexa
outra_expressao_relacional = ((m + n - p) * (p / m) > n) and ((m ** 2) < p) or (n != m + p)
print(f"Outra Expressão Relacional: {outra_expressao_relacional}") 


"""
====== atividade ======

Defina as variáveis a = 7, b = 3, c = 5, d = 2
Execute a expressão matemática complexa:
((a * b) + (c / d)) - (a ** b))
Anote o resultado

Defina as variáveis x = 10, y = 20, z = 30
Execute a expressão condicional:
(x < y and y > z) or (x + y == z and not (z == x * 3))
Determine se a expressão retorna True ou False

Defina as variáveis m = 25, n = 35, p = 45
Crie uma expressão relacional que combine operadores matemáticos, lógicos e de comparação
Execute a expressão:
((m + n) > (p * 2)) and ((p / n) < m) or (n == m + p)
Anote o resultado

"""

a = 7
b = 3
c = 5
d = 2

expressao_matematica_2 = ((a * b) + (c / d)) - (a ** b)
print("expressao_matematica_2: ", expressao_matematica_2)


x = 10
y = 20
z = 30

expressao_condicional_2 = (x < y and y > z) or (x + y == z and not (z == x * 3))
print("expressao_condicional_2: ", expressao_condicional_2)

m = 25
n = 35
p = 45

expressao_relacional_2 = ((m + n) > (p * 2)) and ((p / n) < m) or (n == m + p)
print("expressao_relacional_2: ", expressao_relacional_2)







