
def twoSum(numbers, target):
    esquerda = 0
    direita = len(numbers) - 1

    while esquerda < direita:
        num_esquerda = numbers[esquerda]
        num_direira = numbers[direita]

        soma = num_esquerda + num_direira

        if soma == target:
            return [esquerda + 1, direita + 1]
        elif soma < target:
            esquerda += 1
        else:
            direita -= 1
    return []
    


print(twoSum([1,2,3,4], 3))