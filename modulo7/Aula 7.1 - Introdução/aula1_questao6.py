#Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. Anagramas são palavras com os mesmos caracteres rearranjados.

#Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores

#Digite a palavra objetivo: amor

#Anagramas: ["amor", "mora", "ramo", "Roma"]

from collections import Counter

def encontrar_anagramas(frase, palavra_objetivo):
    palavras = frase.split()
    objetivo_contagem = Counter(palavra_objetivo.lower())
    anagramas = [palavra for palavra in palavras if Counter(palavra.lower()) == objetivo_contagem]

    print(f"Anagramas: {anagramas}")

# Solicita a entrada do usuário
frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")
encontrar_anagramas(frase, palavra_objetivo)
