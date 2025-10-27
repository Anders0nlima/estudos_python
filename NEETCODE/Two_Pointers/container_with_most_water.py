def maxArea(heights):
    esquerda = 0
    direita = len(heights) - 1
    max_area = 0

    while esquerda < direita:
        heights_esquerda = heights[esquerda]
        heights_direita = heights[direita]

        area = min(heights_esquerda, heights_direita) * (direita - esquerda)
        if area > max_area:
            max_area = area
        
        if heights_esquerda < heights_direita:
            esquerda += 1
        else:
            direita -= 1
    return max_area



print(maxArea([2, 2, 2]))
