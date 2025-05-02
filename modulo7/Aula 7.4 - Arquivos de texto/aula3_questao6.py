#Vamos descobrir as músicas mais populares do Spotify nos últimos 10 anos!

#Crie uma conta no Kaggle, uma das principais plataformas de ciência de dados e aprendizado de máquina. Em disciplinas avançadas vamos trabalhar com bases de dados provenientes de lá!

#Baixe o arquivo spotify-2023.csv no final da página que apresenta os dados.

#No Python, abra o arquivo para leitura e imprima as cinco primeiras linhas

#Para abrir o arquivo, defina o parâmetro encoding='latin-1'

#Após compreender a estrutura do arquivo (divisão em colunas, caracter separador de coluna, etc.) passamos para a etapa de extração de informações.

#O arquivo está estruturado da seguinte forma: cada linha representa uma música e contém as seguintes informações separadas por vírgula (CSV):

#track_name,artist(s)_name,artist_count,released_year,released_month,released_day,in_spotify_playlists,in_spotify_charts,streams,in_apple_playlists

#Usaremos apenas informações das colunas:

#track_name

#Nome da música

#artist(s)_name

#Nome do artista

#artist_count

#Número de artistas listados em artist(s)_name

#released_year

#Ano de lançamento

#streams

#Número de vezes que a música foi tocada no Spotify



#Você deve criar um script Python para processar esse arquivo e gerar uma lista com 10 elementos, cada qual representando a música mais tocada de cada ano no intervalo de 2012 a 2022. Considere somente músicas dentro do intervalo solicitado. Cada elemento da lista produzida deve conter as seguintes informações:

#[track_name, artist(s)_name, released_year, streams]

#Essa atividade tem alguns desafios. Assim como as colunas da tabela são separadas por vírgulas, músicas com mais de um artista (artist_count>1) terá o campo artist(s)_name entre aspas com o nome dos artistas separado por vírgulas. Ex:

#Seven (feat. Latto) (Explicit Ver.),"Latto, Jung Kook",2,2023, …

#Há também nomes de músicas entre aspas por conter caracteres especiais como vírgulas ou aspas. Ex:

#"Peso Pluma: Bzrp Music Sessions,Vol.55","Bizarrap,Peso Pluma",2,2023,

#Você deve ignorar essas linhas, e terá portanto que propor uma verificação para identificá-las.

#Ao final imprima a lista produzida. Ex:

#[['When I Was Your Man', 'Bruno Mars', 2012, 1661187319],
# ['I Wanna Be Yours', 'Arctic Monkeys', 2013, 1297026226],
# ...,
# ['As It Was', 'Harry Styles', 2022, 2513188493]]



import csv

# Lista para armazenar as músicas mais tocadas por ano
top_songs_by_year = {}

# Abrindo o arquivo CSV
with open('spotify-2023.csv', 'r', encoding='latin-1') as file:
    reader = csv.reader(file)
    next(reader)  # Pula o cabeçalho

    # Processando cada linha do arquivo
    for row in reader:
        try:
            # Extraindo as colunas relevantes
            track_name = row[0]
            artist_name = row[1]
            artist_count = int(row[2])
            released_year = int(row[3])
            streams = int(row[8])

            # Verifica se o ano está no intervalo 2012-2022
            if 2012 <= released_year <= 2022:
                # Verifica se há aspas no nome da música ou artistas
                # Ignora linhas com múltiplos artistas entre aspas ou nomes complexos
                if (track_name.startswith('"') and track_name.endswith('"')) or \
                        (artist_name.startswith('"') and artist_name.endswith('"')):
                    continue

                # Cria a entrada da música
                song_entry = [track_name, artist_name, released_year, streams]

                # Atualiza a música mais tocada para o ano correspondente
                if released_year not in top_songs_by_year or \
                        streams > top_songs_by_year[released_year][3]:
                    top_songs_by_year[released_year] = song_entry

        except (ValueError, IndexError):
            # Ignora linhas com dados inválidos
            continue

# Cria a lista final ordenada por ano
result = [top_songs_by_year[year] for year in range(2012, 2023)
          if year in top_songs_by_year]

# Imprime as primeiras 5 linhas para verificação inicial
print("Primeiras 5 linhas do arquivo (exemplo de leitura):")
with open('spotify-2023.csv', 'r', encoding='latin-1') as file:
    for i, line in enumerate(file):
        if i < 5:
            print(line.strip())
        else:
            break

print("\nLista das 10 músicas mais tocadas (2012-2022):")
print(result)