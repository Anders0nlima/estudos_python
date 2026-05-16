def diagonais(n):
    return ((n * (n-3))/2)

def somaAngulos(n):
    return (n - 2) * 180

def anguloInterno(n):
    soma = somaAngulos(n)
    return soma/n

n = int(input("Digite o numero de verticais: ")) 

diagonais = diagonais(n)
soma_angulos = somaAngulos(n)
interno = anguloInterno(n)

print(f"Numero de diagonais: {diagonais}")
print(f"a soma dos angulos internos: {soma_angulos}")
print(f"angulo interno: {interno}")

 