for num in range(1000, 9999):
    num_string = str(num)

    num_primeiro = int(num_string[:2])
    num_segundo = int(num_string[2:])

    soma = num_primeiro + num_segundo
    soma_quadrado = soma ** 2

    if soma_quadrado == num:
        print(num)