""" 
2. Soma Máxima Contígua (Kadane's adaptado)

Descrição:
Crie uma função que receba uma lista de inteiros e retorne a maior soma possível de uma subsequência contígua.
Exemplo:
Entrada: [3, -2, 5, -1] → Saída: 6 (sublista [3, -2, 5])
Dica: não use bibliotecas prontas de soma máxima. 

"""

entrada = [3, -2, 5, -1]

def kadene(lista):
    max_soma = lista[0] #guarda a maior soma encontrada atual
    soma_atual = lista[0] #soma acumulada

    for i in range(1, len(lista)):
        soma_atual = max(lista[i], soma_atual + lista[i])
        max_soma = max(max_soma, soma_atual)
    
    return max_soma


print(kadene(entrada))
