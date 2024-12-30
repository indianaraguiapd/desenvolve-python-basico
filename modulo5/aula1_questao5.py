#Você está trabalhando em um sistema de mensagens instantâneas, que deve permitir o uso de emojis nas conversas entre pessoas. Faça:

#No terminal, instale a biblioteca emoji usando o gerenciador de pacotes pip

#$ pip install emoji

 

import emoji  # Importa a biblioteca emoji

# Apresenta a lista de emojis disponíveis ao usuário
print("Emojis disponíveis:")
print("❤️ - :red_heart:")
print("👍 - :thumbs_up:")
print("🤔 - :thinking_face:")
print("🥳 - :partying_face:")

# Solicita ao usuário que insira uma frase codificada com emojis
frase_codificada = input("\nDigite uma frase e ela será emojizada:\n")

# Converte a frase codificada para a versão com os emojis reais
frase_emojizada = emoji.emojize(frase_codificada, language="alias")

# Exibe a frase emojizada
print("\nFrase emojizada:")
print(frase_emojizada)
