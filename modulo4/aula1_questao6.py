

# Inicializar contadores
total_cobaias = 0
total_sapos = 0
total_ratos = 0
total_coelhos = 0

# Ler a quantidade de experimentos registrados
N = int(input("Digite a quantidade de experimentos registrados: "))

# Loop para processar cada experimento
for _ in range(N):
    # Ler a quantidade de cobaias e o tipo
    dados = input("Digite a quantidade e o tipo de cobaia (S, R ou C): ").split()
    quantia = int(dados[0])
    tipo = dados[1]

    # Atualizar o total de cobaias
    total_cobaias += quantia

    # Atualizar o total de cada tipo de cobaia
    if tipo == 'S':
        total_sapos += quantia
    elif tipo == 'R':
        total_ratos += quantia
    elif tipo == 'C':
        total_coelhos += quantia

# Calcular os percentuais
percentual_sapos = (total_sapos / total_cobaias) * 100 if total_cobaias > 0 else 0
percentual_ratos = (total_ratos / total_cobaias) * 100 if total_cobaias > 0 else 0
percentual_coelhos = (total_coelhos / total_cobaias) * 100 if total_cobaias > 0 else 0

# Exibir os resultados
print(f"Total de cobaias utilizadas: {total_cobaias}")
print(f"Total de sapos: {total_sapos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de coelhos: {total_coelhos}")
print(f"Percentual de sapos: {percentual_sapos:.2f}%")
print(f"Percentual de ratos: {percentual_ratos:.2f}%")
print(f"Percentual de coelhos: {percentual_coelhos:.2f}%")
