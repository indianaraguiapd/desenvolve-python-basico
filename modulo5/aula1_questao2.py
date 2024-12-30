#Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e calcule a raíz quadrada da soma dos valores. Peça ao usuário o valor de n

#Biblioteca random: Função randint()

#Biblioteca math:  Função sqrt()

import random  # Importa a biblioteca para gerar números aleatórios
import math    # Importa a biblioteca para cálculos matemáticos

# Solicita ao usuário o número de valores inteiros a serem gerados
n = int(input("Quantos valores inteiros aleatórios você deseja gerar? "))

# Inicializa a soma
soma = 0

# Gera 'n' valores aleatórios entre 0 e 100 e calcula a soma
for _ in range(n):
    valor = random.randint(0, 100)
    soma += valor
    print(f"Valor gerado: {valor}")  # Exibe os valores gerados

# Calcula a raiz quadrada da soma
raiz_quadrada = math.sqrt(soma)

# Exibe o resultado
print(f"\nA soma dos valores gerados é: {soma}")
print(f"A raiz quadrada da soma é: {raiz_quadrada:.2f}")
