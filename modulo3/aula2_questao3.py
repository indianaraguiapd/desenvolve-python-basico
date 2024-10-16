# 3) Você está desenvolvendo um sistema de admissão para um clube juvenil de jogos de tabuleiro. Escreva um programa em Python que pergunte ao usuário sua idade, se já jogou pelo menos 3 jogos de tabuleiro (resposta deve ser True ou False) e quantas vezes venceu um jogo. O programa deve imprimir True, permitindo o ingresso do participante no clube, se:

# Entrada
#idade, se jogou prlo menos 3 jogos de tabuleiro e quantas vezes venceu um jogo
idade = int(input("sua idade é: "))
jogos =  int(input("quantos jogou de tabuleiro já jogou: "))
vitorias =  int(input("quantas vezes venceu um jogo: "))

# Processamento
# a: tiver entre 16 e 18 anos
# B: já tiver jogado pelo menos 3 jogos
# C:já tiver vencido pelo menos 1 jogo
permitido_ingresso =  (16<= idade <= 18) and (jogos == 3) and (vitorias >=1 )
# Saída
print(permitido_ingresso)