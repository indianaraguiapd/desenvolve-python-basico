#Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".

#Digite uma frase: O rato roeu a roupa do rei

#Frase modificada: * r*t* r*** * r**p* d* r**

# Solicita a frase ao usuário
frase = input("Digite uma frase: ")

# Define as vogais (maiúsculas e minúsculas)
vogais = "aeiouAEIOU"

# Substitui cada vogal por *
frase_modificada = ""
for letra in frase:
    if letra in vogais:
        frase_modificada += "*"
    else:
        frase_modificada += letra

# Exibe o resultado
print("Frase modificada:", frase_modificada)