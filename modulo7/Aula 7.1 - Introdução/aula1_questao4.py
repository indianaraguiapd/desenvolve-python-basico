#Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente. Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. Adicione o separador "-" na sua impressão.

#Digite o número: 97651234

#Número completo: 99765-1234

#Digite o número: 980876543

#Número completo: 98087-6543

def formatar_numero(numero):
    numero = numero.strip()

    if len(numero) == 8:  # Se o número tem apenas 8 dígitos, adiciona o 9 na frente
        numero = '9' + numero

    if len(numero) == 9 and numero[0] == '9':  # Garante que o número tenha 9 dígitos e começa com 9
        return numero[:5] + '-' + numero[5:]

    return "Número inválido!"  # Caso não atenda aos critérios

# Entrada do usuário
numero = input("Digite o número: ")
numero_formatado = formatar_numero(numero)
print("Número completo:", numero_formatado)
