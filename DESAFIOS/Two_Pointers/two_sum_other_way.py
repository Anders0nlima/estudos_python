

def twoSum(numbers, target):
    for esquerda in range(len(numbers)):
        for direita in range(esquerda+1, len(numbers)):
            if numbers[esquerda] + numbers[direita] == target:
                return [esquerda+1, direita+1]
    return []





print(twoSum([1,2,3,4], 3))