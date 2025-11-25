num = int(input("Digite um numero entre 1000 e 9999: "))

num_string = str(num)

num_primeiro = num_string[:2]
num_segundo = num_string[2:]

soma = int(num_primeiro) + int(num_segundo)

soma_quadrado = (soma**2)

print(soma_quadrado)