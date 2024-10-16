#leia n1, n2, n3
#n = (n1 + n2 + n3)/3
#m>=60
#se sim imprima " aprovado"
#se não 
#mm>=40 se sim imprima " Recuperação"
#se não imprima "Reprovado"
#caso contrario imprima "Fim"

# Loop para repetir o processo até o usuário decidir parar
while True:
    # Solicita as notas n1, n2 e n3
    n1 = float(input("Digite a nota n1 (ou -1 para sair): "))
    
    # Condição para encerrar o programa
    if n1 == -1:
        print("Fim")
        break

    n2 = float(input("Digite a nota n2: "))
    n3 = float(input("Digite a nota n3: "))

    # Calcula a média
    n = (n1 + n2 + n3) / 3

    # Verifica a situação do aluno
    if n >= 60:
        print("Aprovado")
    elif n >= 40:
        print("Recuperação")
    else:
        print("Reprovado")
