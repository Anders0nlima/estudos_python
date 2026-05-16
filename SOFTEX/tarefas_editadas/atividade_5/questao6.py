n = int(input("numero: "))

h = 0.0

i = 1

while i <= n:
    h += 1 / i
    i += 1

print(f"O valor de h para {n} termos e {h}")