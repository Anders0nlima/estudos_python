def backup_item(lista):
    backup = lista.copy()
    lista.clear()
    print("backup: ", backup)
    print("lista apagada: ", lista)
    
lista = [1, 2, 3, 4, 5]
print("lista apagada", lista)

backup_item(lista)