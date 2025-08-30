preco_fisico_x = 60
por_hora_x = 18

preco_fisico_y = 24
por_hora_y = 36 # calculo

valor_x = preco_fisico_x + (por_hora_x * 2)

limite = (valor_x - preco_fisico_y)/2 >= por_hora_y

if limite:
    print("limite")
else:
    print("nao sei")    