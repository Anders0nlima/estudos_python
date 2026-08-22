idade = int(input())

anos = int(idade/365)
mes = int((idade%365)/30)
dia = int((idade%365)%30)

print(f"{anos} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")
