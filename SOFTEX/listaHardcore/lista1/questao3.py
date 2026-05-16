""" 
3. Remover Elementos Duplicados Sem Usar set()

Descrição:
Crie uma função que receba uma lista e remova duplicatas, mantendo a ordem original.
Exemplo:
Entrada: [1, 2, 1, 3, 2, 4]
Saída: [1, 2, 3, 4] 

"""

def remover_item_duplicado(lista):
    resultado = []
    for item in lista:
        if item not in resultado:
            resultado.append(item)
    return resultado

entrada = [1, 2, 1, 3, 2, 4]

print(remover_item_duplicado(entrada))

