def buscar_item(lista, item):
    try:
        posicao = lista.index(item)
        return f"item encontrado: posição {posicao+1} da lista: {lista}"
    except ValueError:
        return "item nao encontrado"
    
listaNumeros = [1, 2, 3, 4, 5]

busca = int(input("pequise um item: "))

print(buscar_item(listaNumeros, busca))