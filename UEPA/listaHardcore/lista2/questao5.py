from datetime import date, datetime

print("Digite sua data de nascimento no formato: dd/mm/aaaa")
nascimento = input("→ ")

data_nasc = datetime.strptime(nascimento, "%d/%m/%Y").date()

hoje = date.today()

aniversario_este_ano = date(hoje.year, data_nasc.month, data_nasc.day)

if aniversario_este_ano < hoje:
    print("🎂 Seu aniversário já passou este ano!")
    proximo_aniversario = date(hoje.year + 1, data_nasc.month, data_nasc.day)
else:
    print("🎉 Seu aniversário ainda vai chegar!")
    proximo_aniversario = aniversario_este_ano

faltam = (proximo_aniversario - hoje).days

print(f"Faltam {faltam} dias para o seu próximo aniversário 🎈")