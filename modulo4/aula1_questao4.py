#Leia n
#maior = 0
#n > 0
#caso ao contrario imprima "Maior"
#sendo sim leia x 
# x > maior 
# se sim 
#maior = x
#se nao n = n-1


# Inicializar a variável maior
maior = 0

# Ler o número n
n = int(input("Digite quantos números você deseja inserir (n): "))

# Loop enquanto n for maior que 0
while n > 0:
    # Ler o valor de x
    x = float(input("Digite um número (x): "))
    
    # Verificar se x é maior que o maior atual
    if x > maior:
        maior = x  # Atualizar maior se x for maior
    else:
        n -= 1  # Decrementar n se x não for maior

# Imprimir o maior valor encontrado
print(f"Maior: {maior}")
