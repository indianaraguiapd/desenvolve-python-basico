#Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. Dica: usando listas você não precisa fazer um "if" para cada mês.

#Digite uma data de nascimento: 29/10/1973

#Você nasceu em  29 de Outubro de 1973.

# Lista com os meses por extenso
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

# Solicita a data de nascimento
data = input("Digite uma data de nascimento (dd/mm/aaaa): ")

# Separa dia, mês e ano
dia, mes, ano = data.split('/')

# Converte mês de número para extenso (subtrai 1 pois lista começa em 0)
mes_extenso = meses[int(mes) - 1]

# Imprime o resultado
print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")