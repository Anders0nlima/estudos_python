#5.12.3-Faça uma função que calcule a soma dos n primeiros números inteiros e retorne
#uma mensagem se essa soma é par ou impar

def soma_par_impar(n):
    soma = 0
    for i in range(n):
        soma = soma + (i + 1)

    if soma % 2 == 0:
        return f"Par -> {soma}"
    else:
        return f"Impar -> {soma}"
    

print(soma_par_impar(11))