N = int(input())

horas = int(N/3600)
minutos = int((N%3600)/60)
segundos = int(N%60)

print(f"{horas}:{minutos}:{segundos}")