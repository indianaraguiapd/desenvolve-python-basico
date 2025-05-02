#Vamos fazer o jogo da forca! Antes de programar:

#Crie um arquivo no seu computador chamado "gabarito_forca.txt" com uma lista de 10 palavras de sua escolha (separadas por quebras de linha, "\n"). Essas serão as opções de palavra do jogo.

#Crie um arquivo chamado "gabarito_enforcado.txt" com o conteúdo apresentado ao final dessa questão.

#Escreva um programa em Python para executar o jogo, de acordo com as definições:

#Abra o arquivo "gabarito_forca.txt" e escolha aleatoriamente uma palavra;

#Com o arquivo "gabarito_enforcado.txt", crie uma lista de strings com os estágios do enforcado;

#No início exiba o número de letras na palavra como underscores;

#Permita que o jogador insira letras para adivinhar a palavra;

#Em caso de acerto, mostre o progresso do jogador substituindo os underscores correspondentes à letra digitada;

#Em caso de erro, crie a função "imprime_enforcado()" que recebe um inteiro indicando o número de erros do jogador e imprime o enforcado correspondente;

#Limite o número de tentativas para 6 (as partes do enforcado).

# Criando gabarito_forca.txt com 10 palavras
palavras = ["python", "forca", "jogo", "programacao", "inteligencia",
            "artificial", "desafio", "computador", "algoritmo", "tecnologia"]
with open("gabarito_forca.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("\n".join(palavras))

# Criando gabarito_enforcado.txt com os estágios do enforcado
enforcado = [
    "  |---|\n      |\n      |\n      |\n=========",
    "  |---|\n  O   |\n      |\n      |\n=========",
    "  |---|\n  O   |\n  |   |\n      |\n=========",
    "  |---|\n  O   |\n /|   |\n      |\n=========",
    "  |---|\n  O   |\n /|\\  |\n      |\n=========",
    "  |---|\n  O   |\n /|\\  |\n /    |\n=========",
    "  |---|\n  O   |\n /|\\  |\n / \\  |\n========="
]
with open("gabarito_enforcado.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("\n\n".join(enforcado))


import random

# Função para imprimir o enforcado
def imprime_enforcado(erros):
    with open("gabarito_enforcado.txt", "r", encoding="utf-8") as arquivo:
        estagios = arquivo.read().split("\n\n")
    print(estagios[erros])

# Lendo as palavras do gabarito
with open("gabarito_forca.txt", "r", encoding="utf-8") as arquivo:
    palavras = arquivo.read().splitlines()
palavra = random.choice(palavras).lower()

# Inicializando o jogo
erros = 0
tentativas_max = 6
letras_tentadas = set()
progresso = ["_" for _ in palavra]

print("Bem-vindo ao Jogo da Forca!")
print(" ".join(progresso))

# Loop principal do jogo
while erros < tentativas_max and "_" in progresso:
    letra = input("\nDigite uma letra: ").lower()

    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, digite apenas uma letra válida!")
        continue

    if letra in letras_tentadas:
        print("Você já tentou essa letra!")
        continue

    letras_tentadas.add(letra)

    if letra in palavra:
        print("Acertou!")
        for i, char in enumerate(palavra):
            if char == letra:
                progresso[i] = letra
    else:
        erros += 1
        print("Errou!")
        imprime_enforcado(erros)

    print(" ".join(progresso))
    print(f"Tentativas restantes: {tentativas_max - erros}")

# Resultado final
if "_" not in progresso:
    print("\nParabéns! Você venceu!")
else:
    print(f"\nGame Over! A palavra era '{palavra}'.")
    imprime_enforcado(erros)

