#Escreva um programa em Python que utiliza a biblioteca random para gerar um número aleatório entre 1 e 10 e peça ao usuário para adivinhar o número. Forneça feedback se o palpite é muito alto, muito baixo ou correto. Interrompa a execução somente quando o usuário acertar o palpite.


import random  # Importa a biblioteca random para gerar números aleatórios

# Gera um número aleatório entre 1 e 10
numero_aleatorio = random.randint(1, 10)

# Mensagem inicial
print("Adivinhe o número entre 1 e 10.")

while True:
    # Solicita ao usuário que insira um palpite
    palpite = int(input("Seu palpite: "))

    # Verifica o palpite
    if palpite == numero_aleatorio:
        print(f"Correto! O número é {palpite}.")
        break  # Encerra o loop quando o usuário acerta
    elif palpite < numero_aleatorio:
        print("Muito baixo, tente novamente!")
    else:
        print("Muito alto, tente novamente!")
