#leia n
#cont = 0
#se cont = cont + 1 
#imprima "cont", caso ao contrario imprima " fim"

# Inicializar a variável cont
cont = 0

# Loop 'while' que executa enquanto cont for menor que n
n = int(input("Digite o valor de n: "))

while cont < n:
    cont += 1  # Incrementa cont a cada iteração
    print(f"Contador: {cont}")

# Depois que o loop termina
print("Fim!")
