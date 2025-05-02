#Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" e salve em seu computador com o nome "estomago.txt". Em seguida crie um script em Python que abra o arquivo para leitura e imprima:

#O texto das primeiras 25 linhas

#O número de linhas do arquivo

#A linha com maior número de caracteres

#O número de menções aos nomes dos personagens "Nonato" e "Íria" (inclua todas as variações de maiúsculas e minúsculas e atenção para não incluir a substring "iria" se ela fizer parte de outras palavras).

# Abre o arquivo para leitura
with open('estomago.txt', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

# Imprime as primeiras 25 linhas
print("Primeiras 25 linhas do arquivo:")
for i in range(min(25, len(linhas))):
    print(f"Linha {i+1}: {linhas[i].strip()}")

# Calcula o número total de linhas
num_linhas = len(linhas)
print(f"\nNúmero total de linhas no arquivo: {num_linhas}")

# Encontra a linha com o maior número de caracteres
linha_mais_longa = max(linhas, key=len)
print(f"\nLinha com maior número de caracteres ({len(linha_mais_longa)} caracteres):")
print(linha_mais_longa.strip())

# Conta menções aos nomes "Nonato" e "Íria" (case-insensitive, apenas palavras inteiras)
texto_completo = ' '.join(linhas)  # Junta todas as linhas em uma string única
palavras = texto_completo.split()  # Divide em palavras

# Contagem de "Nonato" (inclui variações de maiúsculas e minúsculas)
contagem_nonato = sum(1 for palavra in palavras if palavra.lower() == "nonato")
contagem_iria = sum(1 for palavra in palavras if palavra.lower() == "íria")

print(f"\nNúmero de menções ao nome 'Nonato': {contagem_nonato}")
print(f"Número de menções ao nome 'Íria': {contagem_iria}")