def media_lista():
    lista = []
    for i in range(4):
        notas = int(input(f"{i+1} - Nota: "))
        lista.append(notas)
    print(lista)
    soma = sum(lista)
    tamanho = len(lista)
    media = soma/tamanho
    print(f"Media Geral: {media}")

media_lista()

