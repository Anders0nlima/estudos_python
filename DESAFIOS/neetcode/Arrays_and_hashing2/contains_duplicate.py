def hasDuplicate(nums):
    lista = []
    for i in range(len(nums)):
        lista.append(nums[i])
        sem_duplicados = list(set(lista))

    if len(lista) != len(sem_duplicados):
        return True
    else:
        return False


print(hasDuplicate([1, 2, 3, 4]))