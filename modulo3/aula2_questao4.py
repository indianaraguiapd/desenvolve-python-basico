# 4)Você é mestre de uma mesa de RPG e vai criar um sistema para validar uma ficha de personagem. Cada personagem tem uma classe específica com requisitos de atributos. Escreva um script que solicita a classe de personagem escolhida (guerreiro, mago ou arqueiro), os pontos de força e os pontos de magia atribuídos ao personagem. O programa deve imprimir True se os pontos de atributo são consistentes com a classe escolhida, seguindo as seguintes regras:

# Entrada
# classe: Guerreiro Mago, Arqueiro
# Pontos de força(de 1a 10)
# Pontos de magia (de 1 a 20)

classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
pontos_de_forca =  int(input("Digite os pontos de força (de 1 a 20): "))
pontos_de_magia =  int(input("Digite os pontos de magia:  "))

# Processamento
# Guerreiro: Força deve ser igual ou superior a 15, Magia deve ser 10 ou menos.

# Mago: Força deve ser 10 ou menos, Magia deve ser igual ou superior a 15.

# Arqueiro: Força e Magia devem ser ambos superiores a 5, mas nenhum deles pode ser superior a 15
carta_guerreiro = (1<= pontos_de_forca >15 and (1<= pontos_de_magia  <=10))
carta_mago =(1<= pontos_de_forca >10  and (1<= pontos_de_magia  >15)) 
# Saída
# Ponto de atributo consistentes com a classe escolhida