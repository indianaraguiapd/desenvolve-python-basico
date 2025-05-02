#Escreva um programa que solicita o nome do usuário e o imprime em forma de escada, como indicado no exemplo a seguir.

#Digite seu nome: Fulano

#F

#Fu

#Ful

#Fula

#Fulan

#Fulano

# Solicita o nome do usuário
nome = input("Digite seu nome: ")

# Imprime o nome em forma de escada
for i in range(len(nome)):
    print(nome[:i+1])