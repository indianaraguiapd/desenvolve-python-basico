#Escreva um script que dado uma frase conta os espaços em branco.

#Digite a frase: Meu amor mora em Roma e me deu um ramo de flores

#Espaços em branco: 11



def contar_espacos(frase):
    return frase.count(' ')

# Solicita a frase do usuário
frase = input("Digite a frase: ")

# Conta os espaços em branco
espacos = contar_espacos(frase)

# Exibe o resultado
print(f"Espaços em branco: {espacos}")
