extenso = ""
soma = 0

for i in range(1, 1001):

  num = str(i)

  digitos = len(num)

  d1 = d2 = d3 = d4 = 0

  if digitos == 1:
    d1 = int(num[0])
  elif digitos == 2:
    d1 = int(num[1])
    d2 = int(num[0])
  elif digitos == 3:
    d1 = int(num[2])
    d2 = int(num[1])
    d3 = int(num[0])
  elif digitos == 4:
    d1 = int(num[3])
    d2 = int(num[2])
    d3 = int(num[1])
    d4 = int(num[0])

  num = int(num)

  if d1 == 9:
      extenso = "NOVE"
  elif d1 == 8:
      extenso = "OITO"
  elif d1 == 7:
      extenso = "SETE"
  elif d1 == 6:
      extenso = "SEIS"
  elif d1 == 5:
      extenso = "CINCO"
  elif d1 == 4:
      extenso = "QUATRO"
  elif d1 == 3:
      extenso = "TRES"
  elif d1 == 2:
      extenso = "DOIS"
  elif d1 == 1:
      extenso = "UM"
  elif d1 == 0:
      extenso = ""

  dezena = ""

  if d2 == 2:
      dezena = "VINTE"
  elif d2 == 3:
      dezena = "TRINTA"
  elif d2 == 4:
      dezena = "QUARENTA"
  elif d2 == 5:
      dezena = "CINQUENTA"
  elif d2 == 6:
      dezena = "SESSENTA"
  elif d2 == 7:
      dezena = "SETENTA"
  elif d2 == 8:
      dezena = "OITENTA"
  elif d2 == 9:
      dezena = "NOVENTA"

  if d2 != 0:
    if d1 != 0:
      extenso = dezena + "E" + extenso
    else:
      extenso = dezena + extenso

  if d2 == 1:
      if d1 == 9:
        extenso = "DEZENOVE"
      elif d1 == 8:
        extenso = "DEZOITO"
      elif d1 == 7:
        extenso = "DEZESSETE"
      elif d1 == 6:
        extenso = "DEZESSEIS"
      elif d1 == 5:
        extenso = "QUINZE"
      elif d1 == 4:
        extenso = "QUATORZE"
      elif d1 == 3:
        extenso = "TREZE"
      elif d1 == 2:
        extenso = "DOZE"
      elif d1 == 1:
        extenso = "ONZE"
      elif d1 == 0:
        extenso = "DEZ"

  centena = ""

  if d3 == 1 and d2 == 0 and d1 == 0:
      centena = "CEM"
  elif d3 == 1:
      centena = "CENTO"
  elif d3 == 2:
      centena = "DUZENTOS"
  elif d3 == 3:
      centena = "TREZENTOS"
  elif d3 == 4:
      centena = "QUATROCENTOS"
  elif d3 == 5:
      centena = "QUINHENTOS"
  elif d3 == 6:
      centena = "SEISCENTOS"
  elif d3 == 7:
      centena = "SETECENTOS"
  elif d3 == 8:
      centena = "OITOCENTOS"
  elif d3 == 9:
      centena = "NOVECENTOS"

  if d3 != 0:
    if d2 != 0 or d1 != 0:
        extenso = centena + "E" + extenso
    else:
        extenso = centena + extenso

  if num == 1000:
      extenso = "MIL" + extenso

  print(extenso)

  soma += len(extenso)
  extenso = ""

print("A soma das letras utilizadas contando de 1 a 1000 é: ", soma)