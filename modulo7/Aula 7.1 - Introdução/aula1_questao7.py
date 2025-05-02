#Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, bem como a chave da criptografia. Regras:

#Chave de criptografia: gere um valor n aleatório entre 1 e 10

#Substitua cada caracter c pelo caracter c + n. Trabalharemos apenas com o intervalo de caracteres visíveis (entre 33 e 126 na tabela Unicode)

#nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

#chave_aleatoria = 5

#nomes_cript = ['Qzfsf', 'Oz', 'If{n', '[n{n', 'Uwn', 'Qzn!']

import random

def encrypt(nomes):
    n = random.randint(1, 10)  # Gera um valor aleatório entre 1 e 10
    nomes_cript = []

    for nome in nomes:
        nome_cript = "".join(
            chr(((ord(c) - 33 + n) % 94) + 33) for c in nome
        )
        nomes_cript.append(nome_cript)

    return nomes_cript, n

# Testando a função
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave = encrypt(nomes)
print(f"Nomes criptografados: {nomes_criptografados}")
print(f"Chave de criptografia: {chave}")
