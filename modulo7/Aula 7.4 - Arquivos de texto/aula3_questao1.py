#Escreva um script Python que solicita uma frase do usuário e a salve em um arquivo chamado "frase.txt" no mesmo local do seu script. Imprima em seguida o caminho completo do arquivo salvo.

#Digite uma frase: Bom dia, meu nome é Davi.

#Frase salva em /Users/laranjeira/python-basico/frase.txt

import os

# Solicita a frase do usuário
frase = input("Digite uma frase: ")

# Salva a frase em um arquivo chamado "frase.txt"
with open("frase.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(frase)

# Obtém o caminho completo do arquivo
caminho_completo = os.path.abspath("frase.txt")

# Imprime o caminho completo
print(f"Frase salva em {caminho_completo}")