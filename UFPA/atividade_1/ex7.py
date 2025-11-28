hora_entrada = int(input("Horas da entrada: ")) # -> 12
minutos_entrada = int(input("Minutos da entrada: ")) # -> 50

hora_saida = int(input("Horas da entrada: ")) # -> 14
minutos_saida = int(input("Minutos da entrada: ")) # -> 00 

total_minutos_entrada = ((hora_entrada*60) + minutos_entrada) # -> 770
total_minutos_saida = ((hora_saida*60) + minutos_saida) # -> 840

if total_minutos_saida < total_minutos_entrada: #pra nao dá confusoa com o dia seguite 
    total_minutos_saida += 24 * 60
    
total_minutos = total_minutos_saida - total_minutos_entrada

horas_totais = (total_minutos//60) 
minutos_totais = (total_minutos%60)

print(f"Você ficou {horas_totais} hora(s) e {minutos_totais} minuto(s)")

if horas_totais <= 2:
    print("Taxa de R$ 1.0") 
elif horas_totais <= 3:
    print("Taxa de R$ 1.40")
else:
    print("Taxa de R$ 2.0")