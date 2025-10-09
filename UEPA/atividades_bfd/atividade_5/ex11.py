l1 = [2, 5, 8, 6, 4]
l2 = [10, 3, 12, 7, 11]

cont = 0

while cont <= 4:
    l1[cont] = l2[4 - cont]
    cont += 1

#l1[2] = l2[2] 
# 0          4
# 1          3
# 2          2
# 3          1
# 4          0
# crescendo   descrecendo  

print(l1)