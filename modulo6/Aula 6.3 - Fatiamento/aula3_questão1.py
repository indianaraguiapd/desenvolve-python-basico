
#Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (com pelo menos 4 valores), os armazena em uma lista e, usando fatiamento de listas, imprima:

#A lista original

#Os 3 primeiros elementos

#Os 2 últimos elementos

#A lista invertida (do fim para o começo)

#Os elementos de índice par (0, 2, 4 … )

#Os elementos de índice ímpar (1, 3, 5, … )

# Solicita ao usuário uma quantidade indefinida de números inteiros
numeros = []
print("Digite pelo menos 4 números inteiros. Digite 'sair' para finalizar.")

while True:
    entrada = input("Digite um número: ")
    if entrada.lower() == 'sair':
        if len(numeros) >= 4:
            break
        else:
            print("Você precisa digitar pelo menos 4 números.")
            continue
    try:
        numeros.append(int(entrada))
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

# Imprime as informações solicitadas
print("\nLista original:", numeros)
print("Os 3 primeiros elementos:", numeros[:3])
print("Os 2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Elementos de índice par:", numeros[::2])
print("Elementos de índice ímpar:", numeros[1::2])
