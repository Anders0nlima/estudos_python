def duplicado(lista_num):
    lista_vista = set()

    for i in lista_num:
        if i in lista_vista:
            return True
        lista_vista.add(i)
    return False 

print(duplicado([1,2,3,4]))    

