#Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente.
#Em seguida encontre o intervalo que possui a maior quantidade de números negativos
# e delete ele da lista com o operador del. Você deve imprimir a lista antes e após apagar o intervalo.



import random


# Criando lista com 20 elementos aleatórios entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]
print("Lista original:", lista)

# Função para encontrar o intervalo com mais números negativos
def encontrar_intervalo_negativo(lst):
    max_negativos = 0
    inicio_max = 0
    fim_max = 0

    # Testa todos os possíveis intervalos
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublista = lst[i:j]
            contagem_negativos = sum(1 for x in sublista if x < 0)
            if contagem_negativos > max_negativos:
                max_negativos = contagem_negativos
                inicio_max = i
                fim_max = j

    return inicio_max, fim_max

# Encontrando o intervalo
inicio, fim = encontrar_intervalo_negativo(lista)
print(f"Intervalo com mais números negativos: {lista[inicio:fim]} (índices {inicio} a {fim-1})")

# Deletando o intervalo
del lista[inicio:fim]
print("Lista após remoção:", lista)