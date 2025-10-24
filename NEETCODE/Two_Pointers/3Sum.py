

def threeSum(nums):
    esquerda = 0
    direita = len(nums) - 1

    while esquerda < direita:
        num_esquerda = nums[esquerda]
        num_direita = nums[direita]

        if num_esquerda + num_direita == 0:
            return [num_direita, num_direita]
    return []


print(threeSum([-1,0,1,2,-1,-4]))