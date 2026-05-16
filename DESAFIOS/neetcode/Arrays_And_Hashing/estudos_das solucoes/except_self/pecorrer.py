import math

def remover_item(lista):
    resultado = []
    
    for i in range(len(lista)):
        esquerda = lista[:i]
        direita = lista[i + 1:]

        nova_lista = esquerda + direita
        resultado.append(nova_lista)
    
    produtos = []
    for j in resultado:
        produto_atual = math.prod(j)
        produtos.append(produto_atual)

    return produtos
    
print(remover_item([-1,0,1,2,3]))

