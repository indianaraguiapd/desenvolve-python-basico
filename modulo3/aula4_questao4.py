#4) Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
#                Entrada
distancia = float(input("Digite a distância da entrega: "))
peso = float(input("Digite o peso do pacote (kg)"))

#               processo
#Distância até 100 km: R$1 por kg.
#Distância entre 101 e 300 km: R$1.50 por kg.
#Distância acima de 300 km: R$2 por kg.
if distancia <= 100:
    frete = 1 * peso
elif 101 <= distancia <= 300:
    frete = 1.50 *peso
else: 
    frete = 2 * peso
#Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg
if peso > 10:
      frete += 10


#              saída
print(f"O valor do frete é: R${frete: .2f}")