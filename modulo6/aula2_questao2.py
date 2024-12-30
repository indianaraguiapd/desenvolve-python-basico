#Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada num_elementos. Em seguida gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos, e armazene em uma lista chamada elementos. Em seguida imprima:

#.A lista elementos

#.A soma dos valores da lista

#.A média dos valores da lista


import random  # Importa a biblioteca random para gerar números aleatórios

# Gera aleatoriamente um valor entre 5 e 20 para o número de elementos
num_elementos = random.randint(5, 20)

# Gera aleatoriamente 'num_elementos' valores entre 1 e 10 e armazena em uma lista
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Calcula a soma dos valores da lista
soma = sum(elementos)

# Calcula a média dos valores da lista
media = soma / num_elementos

# Imprime os resultados
print("Lista elementos:")
print(elementos)

print("\nSoma dos valores da lista:")
print(soma)

print("\nMédia dos valores da lista:")
print(media)
