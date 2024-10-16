# Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade (>17). Escreva um programa que solicite as idades de Juliana e Cris e imprima True se ambas forem maiores de 17 anos, indicando que podem entrar no bar, e False caso contrário.

#entradas de dados
#idade Juliana
#idade de Cris
idade_juliana = int(input("digite a idade de Juliana:"))
idade_cris = int(input("digite a idade de Cris: "))


# processamento e saida
# True se abos forem maiores de idadde
# <expl1> juliana é maior de idade
#<expl2> Cris é maior de idade
#<expl1> and <expl2>
# False em qualquer outro caso
pode_entrar = idade_juliana >= 17 and idade_cris >= 17

#saisa
#imprima se ambos podem entrar ou nao
print(pode_entrar)
