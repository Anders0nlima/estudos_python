valor = float(input())

centavos = int(round(valor * 100))

n100 = centavos // 10000
centavos = centavos % 10000

n50 = centavos // 5000
centavos = centavos % 5000

n20 = centavos // 2000
centavos = centavos % 2000

n10 = centavos // 1000
centavos = centavos % 1000

n5 = centavos // 500
centavos = centavos % 500

n2 = centavos // 200
centavos = centavos % 200

m1 = centavos // 100
centavos = centavos % 100

m050 = centavos // 50
centavos = centavos % 50

m025 = centavos // 25
centavos = centavos % 25

m010 = centavos // 10
centavos = centavos % 10

m005 = centavos // 5
centavos = centavos % 5

m001 = centavos // 1

print(f"""NOTAS:
{n100} nota(s) de R$ 100.00
{n50} nota(s) de R$ 50.00
{n20} nota(s) de R$ 20.00
{n10} nota(s) de R$ 10.00
{n5} nota(s) de R$ 5.00
{n2} nota(s) de R$ 2.00
MOEDAS:
{m1} moeda(s) de R$ 1.00
{m050} moeda(s) de R$ 0.50
{m025} moeda(s) de R$ 0.25
{m010} moeda(s) de R$ 0.10
{m005} moeda(s) de R$ 0.05
{m001} moeda(s) de R$ 0.01""")
