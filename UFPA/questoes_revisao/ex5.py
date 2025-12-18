for i in range(10, 100):
    num_str = str(i)
    num1 = int(num_str[0])
    num2 = int(num_str[1])

    if ((num1 + num2) * 7) == i:
        print(i)
