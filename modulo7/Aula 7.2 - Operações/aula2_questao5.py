#Implemente uma função chamada embaralhar_palavras() que recebe uma frase como entrada e retorna uma nova frase com as letras internas de cada palavra embaralhadas. Mantenha sempre o primeiro e último caractere da palavra no lugar.
#Dica: use a biblioteca random.

#def embaralhar_palavras(frase):

#### Escreva a função


# Exemplo de uso:

#frase = "Python é uma linguagem de programação"

#resultado = embaralhar_palavras(frase)

#print(resultado)

# Possível saída: "Ptohyn é uma lignaugem de prarmoagãço"

import random

def embaralhar_palavras(frase):
    # Divide a frase em palavras
    palavras = frase.split()

    # Lista para armazenar as palavras embaralhadas
    resultado = []

    for palavra in palavras:
        # Se a palavra tem 3 ou menos caracteres, mantém como está
        if len(palavra) <= 3:
            resultado.append(palavra)
        else:
            # Pega o primeiro e último caractere
            primeiro = palavra[0]
            ultimo = palavra[-1]

            # Pega os caracteres do meio
            meio = list(palavra[1:-1])

            # Embaralha os caracteres do meio
            random.shuffle(meio)

            # Junta tudo: primeiro + meio embaralhado + último
            palavra_embaralhada = primeiro + ''.join(meio) + ultimo
            resultado.append(palavra_embaralhada)

    # Junta as palavras de volta em uma frase
    return ' '.join(resultado)

# Exemplo de uso:
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)