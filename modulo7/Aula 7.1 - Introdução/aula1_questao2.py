#Escreva um programa que solicite ao usuário inserir seu primeiro nome e sobrenome separadamente. Em seguida, concatene essas duas strings e exiba a mensagem de boas-vindas.

#Digite seu primeiro nome: Alice

#Digite seu sobrenome: Silva

#Bem-vinda, Alice Silva!


# Solicita o primeiro nome e sobrenome do usuário
primeiro_nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")

# Concatena as duas strings com um espaço entre elas
nome_completo = primeiro_nome + " " + sobrenome

# Exibe a mensagem de boas-vindas
print("Bem-vindo,", nome_completo + "!")