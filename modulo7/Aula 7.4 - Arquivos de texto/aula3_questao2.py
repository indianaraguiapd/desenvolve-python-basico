#Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt", removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha. Ao final, imprima o conteúdo do arquivo "palavras.txt".

#Bom

#dia

#meu

#nome

#é

#Davi

import re

# Lê o conteúdo do arquivo frase.txt
with open("frase.txt", "r", encoding="utf-8") as arquivo_entrada:
    frase = arquivo_entrada.read()

# Remove caracteres não alfabéticos e separa em palavras
# Usa regex para manter apenas letras e converte para minúsculas
palavras = re.findall(r'[a-zA-Z]+', frase)

# Salva cada palavra em uma linha no arquivo palavras.txt
with open("palavras.txt", "w", encoding="utf-8") as arquivo_saida:
    for palavra in palavras:
        arquivo_saida.write(palavra + "\n")

# Lê e imprime o conteúdo do arquivo palavras.txt
with open("palavras.txt", "r", encoding="utf-8") as arquivo_saida:
    conteudo = arquivo_saida.read()
    print(conteudo)