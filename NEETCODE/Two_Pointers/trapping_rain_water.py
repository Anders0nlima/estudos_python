def trap(height):
    max_esquerda = 0
    max_direita = len(height) - 1

    lista_esquerda = []
    for i in range(len(height) - 1):
        valor_maximo = max(height[i], height[i+1])
        lista_esquerda.append(valor_maximo)

    return lista_esquerda





print(trap([0,2,0,3,1,0,1,3,2,1]))