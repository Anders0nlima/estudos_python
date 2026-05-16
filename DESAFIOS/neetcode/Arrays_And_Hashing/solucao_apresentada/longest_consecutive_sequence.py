
def logest_sequence(nums):
    if not nums:
        return 0
    
    cont = 1
    best = 0 
    ordem = sorted(set(nums)) 
    for i in range(len(ordem) - 1):
        if ordem[i] + 1 == ordem[i+1]:
            cont += 1
        else:
            if cont > best:
                best = cont
            cont = 1
    best = max(best, cont)
    return best

print(logest_sequence([0,3,2,5,4,6,1,1]))


