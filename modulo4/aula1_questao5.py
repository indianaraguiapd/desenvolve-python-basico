#
#Um instituto realizou uma pesquisa de público e precisa calcular a média de idade dos respondentes. Escreva um programa que leia um inteiro N com a quantidade de respondentes e em seguida leia as N idades de cada respondente. Ao final, imprima a média das idades.
#(idade1 + idade2 + idade3 + … + idade_n)/N

n = int(input())

soma = 0 #iniciar as variaveis
cont = 0 #resultado -> soma

while cont < n:
   idade = int(input())
   soma += idade #soma = soma + idade
    # variavel de controle de laço
   cont += 1 #cont = cont -1

   #imprima a media
   print(soma)
   print(soma/n)