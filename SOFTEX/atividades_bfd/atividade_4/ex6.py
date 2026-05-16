preco_fisico_x = 60
por_hora_x = 18

preco_fisico_y = 24


valor_x_2h = preco_fisico_x + (por_hora_x * 2)

limite = (valor_x_2h - preco_fisico_y)/2 

print(f"Deve cobrar na maxima: {limite:.2f} por hora") 