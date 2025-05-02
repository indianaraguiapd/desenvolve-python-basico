#A extensão ".csv" significa "comma-separated values" ou "valores separados por vírgula". É a extensão utilizada por sistemas de gerência de tabelas como o Microsoft Excel ou Google Sheets. Nesse exercício vamos criar uma planilha com dados sobre livros que você já leu ou gostaria de ler. Siga as instruções.

#Selecione pelo menos 10 livros que você leu ou gostaria de ler. Você deve reunir as seguintes informações: título, autor, ano de publicação e número de páginas.

#No Python, crie um arquivo chamado "meus_livros.csv", aberto para escrita.

#Na primeira linha escreva os títulos da planilha separados por vírgula (sem espaço em branco). Os títulos são: "Título", "Autor", "Ano de publicação" e "Número de páginas". Lembre de finalizar a linha com uma quebra de linha.

#A partir da segunda linha escreva as informações de cada livro que você levantou, separando cada informação por uma vírgula (sem espaço em branco). Lembre de finalizar cada linha com uma quebra de linha.

#Feche o arquivo para salvá-lo e abra com a ferramenta de planilhas de sua escolha. Como você já tem conta no Google, sugiro abrir com o Google Sheets.

#Seu arquivo deve ser aberto como uma planilha parecida com essa:

#Título

#Autor

#Ano de publicação

#Número de páginas

#O Caçador de Pipas

#Khaled Hosseini

#2003

#368

#Torto Arado

#Itamar Vieira Junior

#2019

#264


import csv

# Lista de livros como uma lista de dicionários
livros = [
    {"Título": "O Caçador de Pipas", "Autor": "Khaled Hosseini", "Ano de publicação": 2003, "Número de páginas": 368},
    {"Título": "Torto Arado", "Autor": "Itamar Vieira Junior", "Ano de publicação": 2019, "Número de páginas": 264},
    {"Título": "1984", "Autor": "George Orwell", "Ano de publicação": 1949, "Número de páginas": 328},
    {"Título": "Dom Casmurro", "Autor": "Machado de Assis", "Ano de publicação": 1899, "Número de páginas": 256},
    {"Título": "A Revolução dos Bichos", "Autor": "George Orwell", "Ano de publicação": 1945, "Número de páginas": 152},
    {"Título": "O Pequeno Príncipe", "Autor": "Antoine de Saint-Exupéry", "Ano de publicação": 1943, "Número de páginas": 96},
    {"Título": "Cem Anos de Solidão", "Autor": "Gabriel García Márquez", "Ano de publicação": 1967, "Número de páginas": 448},
    {"Título": "A Menina que Roubava Livros", "Autor": "Markus Zusak", "Ano de publicação": 2005, "Número de páginas": 480},
    {"Título": "O Senhor dos Anéis", "Autor": "J.R.R. Tolkien", "Ano de publicação": 1954, "Número de páginas": 1216},
    {"Título": "Sapiens", "Autor": "Yuval Noah Harari", "Ano de publicação": 2011, "Número de páginas": 443}
]

# Criando o arquivo CSV
with open('meus_livros.csv', 'w', newline='') as arquivo:
    # Definindo os nomes das colunas
    colunas = ["Título", "Autor", "Ano de publicação", "Número de páginas"]

    # Criando o escritor CSV
    escritor = csv.DictWriter(arquivo, fieldnames=colunas)

    # Escrevendo o cabeçalho
    escritor.writeheader()

    # Escrevendo os dados dos livros
    escritor.writerows(livros)

print("Arquivo 'meus_livros.csv' criado com sucesso!")

