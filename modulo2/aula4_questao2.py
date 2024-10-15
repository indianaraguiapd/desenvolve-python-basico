#2) Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
#Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e F o valor em Fahrenheit. Antes de imprimir, converta o valor em Celsius para inteiro. A mensagem deve estar formatada da seguinte maneira:


# Lê o valor da temperatura em Fahrenheit (inteiro)
fahrenheit = int(input("Digite a temperatura em graus Fahrenheit: "))

# Converte a temperatura de Fahrenheit para Celsius
celsius = int((fahrenheit - 32) * (5 / 9))

#86 graus Fahrenheit são 30 graus Celsius
# Imprime o resultado formatado
print(f"{fahrenheit} graus Fahrenheit são {celsius} graus Celsius")

