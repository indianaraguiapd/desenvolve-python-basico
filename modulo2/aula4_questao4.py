#) Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível de notas necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2,
# Lê o valor inteiro em reais
#1. A saída deve estar formatada exatamente como indicado. 

#Entrada:
#576

#Saída:
#5 nota(s) de R$100,00
#1 nota(s) de R$50,00
#1 nota(s) de R$20,00
#0 nota(s) de R$10,00
#1 nota(s) de R$5,00
#0 nota(s) de R$2,00
#1 nota(s) de R$1,00

valor = int(input("Digite o valor em reais: "))

# Calcula a quantidade de notas de 100
notas_100 = valor // 100
valor = valor % 100

# Calcula a quantidade de notas de 50
notas_50 = valor // 50
valor = valor % 50

# Calcula a quantidade de notas de 20
notas_20 = valor // 20
valor = valor % 20

# Calcula a quantidade de notas de 10
notas_10 = valor // 10
valor = valor % 10

# Calcula a quantidade de notas de 5
notas_5 = valor // 5
valor = valor % 5

# Calcula a quantidade de notas de 2
notas_2 = valor // 2
valor = valor % 2

# Exibe a quantidade de cada nota necessária
print(f"Nota(s) de 100: {notas_100}")
print(f"Nota(s) de 50: {notas_50}")
print(f"Nota(s) de 20: {notas_20}")
print(f"Nota(s) de 10: {notas_10}")
print(f"Nota(s) de 5: {notas_5}")
print(f"Nota(s) de 2: {notas_2}")

