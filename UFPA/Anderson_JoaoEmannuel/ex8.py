n = int(input("n -> ")) #6
i = int(input("i -> ")) #2
j = int(input("j -> ")) #3

count = 0
k = 0

while count < n:
    if k % i == 0 or k % j == 0:
        print(k)
        count += 1
    k += 1
