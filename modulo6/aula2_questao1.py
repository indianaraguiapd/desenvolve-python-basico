
#Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. Em seguida imprima na ordem estabelecida:

#.A lista ordenada, sem modificar a lista original

#.A lista original

#.O índice do maior valor da lista

#.O índice do menor valor da lista



import random  # Importa a biblioteca random para gerar números aleatórios

# Gera 20 valores inteiros aleatórios entre -100 e 100 e os armazena em uma lista
lista = [random.randint(-100, 100) for _ in range(20)]

# Ordena a lista sem modificar a lista original
lista_ordenada = sorted(lista)

# Encontra os índices do maior e do menor valor da lista
indice_maior = lista.index(max(lista))
indice_menor = lista.index(min(lista))

# Imprime os resultados
print("Lista ordenada (sem modificar a original):")
print(lista_ordenada)

print("\nLista original:")
print(lista)

print(f"\nO índice do maior valor ({max(lista)}) é: {indice_maior}")
print(f"O índice do menor valor ({min(lista)}) é: {indice_menor}")
