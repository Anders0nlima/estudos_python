#1. Faça um programa em Python que peça do usuário um número e então mostra a seguinte mensagem: ‘O número informado foi <numero>’ 

num = int(input("Número: "))
print(f"O número informado foi {num}")

#2. Faça um programa em Python que peça dois valores e imprima a soma desses valores. 

num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))

soma = num1 + num2
print(f"Soma: {soma}")

#3. Faça um programa em Python que peça três valores e imprima na tela a média desses valores.

num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Terceiro número: "))

media = (num1+num2+num3)/3

print(f"A media foi: {media}")


#4. Faça um programa em Python que solicite um comprimento em metros e o programa converte para centímetro. Imprima na tela a conversão ocorrida. 

com_metros = int(input("Valor: "))
com_centimetro = com_metros * 100
print(f"O valor {com_metros} metros equivale a {com_centimetro} centimetros")

#5. Faça um programa em Python que calcule a área de um quadrado. Os valores das medidas serão fornecidas pelo usuário. Mostre na tela o resultado. 

lado = int(input("Valor: "))
area_quadrado = lado * lado 

print(f"a area de quadrado de lado {lado} centimetros é {area_quadrado}")

#6. Faça um programa em Python que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. 

valor_por_hora = int(input("valor a hora: "))
horas_trabalhadas = int(input("horas de trabalho por dia: "))
mes = 30

horas_totais = horas_trabalhadas * mes 

salario = valor_por_hora * horas_totais

print(f"O salaria mensal é {salario}")


#7. Faça um programa que peça dois números inteiros e um número real. Calcule e mostre: 
# → O produto do dobro do primeiro com metade do segundo. 
# → A soma do triplo do primeiro com o terceiro 
# → O terceiro elevado ao cubo.

valor1 = int(input("valor do primeiro inteiro:"))
valor2 = int(input("valor do segundo inteiro:"))
valor3 = float(input("valor do primeiro real:"))

pri = (2*(valor1))*((valor2)/2)
seg = (3*(valor1)) + valor3
ter = (valor3**3)

print(f"O produto do dobro do primeiro com metade do segundo: {pri}")
print(f"A soma do triplo do primeiro com o terceiro: {seg}")
print(f"O terceiro elevado ao cubo: {ter}")