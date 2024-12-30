#Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e calcule a diferença absoluta entre esses dois números. Utilize a função nativa abs para garantir que o resultado seja sempre positivo e round para arredondar o resultado para duas casas decimais.
#exemplo de interação:
#Digite o primeiro número: 3.1415
#Digite o segundo número: 1.4142
#A diferença absoluta entre os números é: 1.73

# Programa para calcular a diferença absoluta entre dois números decimais

# Solicita ao usuário que insira dois números decimais
numero1 = float(input("Insira o primeiro número decimal: "))
numero2 = float(input("Insira o segundo número decimal: "))

# Calcula a diferença absoluta usando a função nativa abs
diferenca = abs(numero1 - numero2)

# Arredonda o resultado para duas casas decimais usando a função nativa round
diferenca_arredondada = round(diferenca, 2)

# Exibe o resultado
print(f"A diferença absoluta entre os dois números é: {diferenca_arredondada}")
