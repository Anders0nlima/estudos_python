def numero_perfeito(num):
    lista_num = []
    for i in range(1, num):
        if num % i == 0:
            lista_num.append(i)
    
    soma = sum(lista_num)
    
    if soma == num:
        return f"o número {num} é perfeito" 
    else:
        return f"o número {num} não é perfeito" 

try:
    num_input = int(input("digite um numero: "))
    print(numero_perfeito(num_input))
except ValueError:
    print("Erro: voce deve digitar um numero")



#utilize o return no try e execept
#a função pode conversar com outra função (fazer isso)
#faça as importações das funções "import"
