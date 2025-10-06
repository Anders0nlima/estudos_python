""" 
4. Matriz Espiral (Spiral Matrix)

Descrição:
Dada uma matriz 2D (lista de listas), retorne todos os elementos na ordem espiral (sentido horário).
Exemplo:
Entrada:

[
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]


Saída: [1,2,3,6,9,8,7,4,5] 

"""

def spiral_order(matriz):
    if not matriz or not matriz[0]:
        return []
    
    top = 0
    botton = len(matriz) - 1
    left = 0
    right = len(matriz[0]) - 1 

    result = []

    while top <= botton and left <= right:
        for col in range(left, right + 1):
            result.append(matriz[top][col])
        top += 1

        for row in range(top, botton + 1):
            result.append(matriz[row][right])
        right -= 1 

        if top <= botton:
            for col in range(right, left - 1, -1):
                result.append(matriz[botton][col])
            botton -= 1

        if left <= right:
            for row in range(botton, top - 1, -1):
                result.append(matriz[row][left])
            left += 1

    return result

matriz_lista = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(spiral_order(matriz_lista))