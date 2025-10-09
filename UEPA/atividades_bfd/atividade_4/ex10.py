print("=== Relação do ano de nascimento ====")

#a
print("1- Qual dia e mês do seu nascimento: ")
dia = int(input("Dia -> "))
mes = int(input("Mês -> "))

string_dia = str(dia)
string_mes = str(mes)

soma_dias = 0
soma_meses = 0

for digito in string_dia:
    soma_dias += int(digito)
    total_dias = soma_dias
for digito in string_mes:
    soma_meses += int(digito)
    total_meses = soma_meses

passo_um = total_dias + total_meses
#print(passo_um)

#b
print("2- Qual o ano atual: ")
ano = int(input("Ano -> "))

string_ano = str(ano)

soma_anos = 0

for digitos in string_ano:
    soma_anos += int(digitos)
    total_anos = soma_anos
#print(total_anos)

#c
resultado = passo_um + total_anos
#print (resultado)

#d 
valor = str(resultado)
soma_resoltado = 0

for digitos in valor:
    soma_resoltado += int(digitos)
    numero = soma_resoltado
#print(numero)

match numero:
    case 1: 
        print("Ano Pessoal 1: é o início de um novo ciclo. Além disso, este é um ano de ação, determinação e realização e direcionar sua energia para alcançar sonhos e metas de longo prazo")
    case 2:
        print("Ano Pessoal 2: é tempo de explorar as relações interpessoais. Além disso, é um período em que as questões de equilíbrio, diplomacia e relacionamentos serão destacadas.")
    case 3:
        print("Ano Pessoal 3: fase de oportunidade para brilhar, expressar habilidades criativas e comunicativas.Além disso, este é um ano em que você estará atraindo atenção.")
    case 4: 
        print("Ano Pessoal 4: este ciclo traz intensificação de realização, planejamento e segurança. É um ano emque se pode alcançar um novo nível de estabilidade se você focar nisso.")
    case 5:
        print("Ano Pessoal 5: ano ótimo para aproveitar o poder de concretização para implementar as mudanças que você deseja ou para se adaptar às mudanças que estão ocorrendo")
    case 6:
        print("Ano Pessoal 6: período ótimo para trabalhar em equipe e de fazer algo significativo para a sociedade, comunidade, família e par.")
    case 7:
        print("Ano Pessoal 7: fase de autoaperfeiçoamento e aprofundamento. Importante focar em como você pode se tornar uma autoridade em sua área de atuação.")
    case 8:
        print("Ano Pessoal 8: ano extremamente poderoso porque está associado a poder, dinheiro, sucesso eautoridade. É uma fase de grande potencial e desafios.")
    case 9:
        print("Ano Pessoal 9: tempo de fechar ciclos, mas também grande potencial para realizações e conquistas")
    case _:
        print("invalido")