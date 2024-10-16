# 2) Dando continuidade à questão anterior, um outro bar permite a entrada de grupos onde pelo menos uma pessoa é maior de idade (ficando responsável pelas outras). Ajuste sua resposta da questão anterior, ainda solicitando as idades de Juliana e Cris, mas ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar, e False caso contrário.

#entradas de dados
#idade Juliana
#idade de Cris
idade_juliana = int(input("digite a idade de Juliana:"))
idade_cris = int(input("digite a idade de Cris:"))


# processamento e saida
# True pelo menos um dois dois forem maiores de idadde
# <expl1> juliana é maior de idade
#<expl2> Cris é maior de idade
#<expl1> and <expl2>
# False em qualquer outro caso
pode_entrar = idade_juliana > 17 or idade_cris > 17

#saisa
print(pode_entrar)
