#Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.

#Exemplo de interação via terminal (entradas em laranja): 

#Digite a quantidade de elementos da lista 1: 4
#Digite os 4 elementos da lista 1:
#1, 2, 3, 4

#Digite a quantidade de elementos da lista 2: 6

#Digite os 6 elementos da lista 2:
#5,6,7,8,9,10

#Lista intercalada: 1 5 2 6 3 7 4 8 9 10

 # Recebe a quantidade de elementos para a lista 1 e os elementos dessa lista
qtd_lista1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = []
print(f"Digite os {qtd_lista1} elementos da lista 1:")
for _ in range(qtd_lista1):
    lista1.append(int(input()))

# Recebe a quantidade de elementos para a lista 2 e os elementos dessa lista
qtd_lista2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = []
print(f"Digite os {qtd_lista2} elementos da lista 2:")
for _ in range(qtd_lista2):
    lista2.append(int(input()))

# Cria uma nova lista intercalada
lista_intercalada = []

# Intercala os elementos das duas listas
for i in range(min(qtd_lista1, qtd_lista2)):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

# Adiciona os elementos remanescentes da maior lista
if qtd_lista1 > qtd_lista2:
    lista_intercalada.extend(lista1[len(lista2):])
elif qtd_lista2 > qtd_lista1:
    lista_intercalada.extend(lista2[len(lista1):])

# Exibe a lista intercalada
print("\nLista intercalada:", ' '.join(map(str, lista_intercalada)))
