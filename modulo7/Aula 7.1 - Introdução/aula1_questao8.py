#Desenvolva um validador de CPF. Solicite do usuário um CPF na forma XXX.XXX.XXX-XX (lido como string) e imprima "Válido" ou "Inválido".

#O primeiro passo é calcular o primeiro dígito verificador. Separamos os primeiros 9 dígitos do CPF (ex: 111.444.777) e multiplicamos cada um dos números, da direita para a esquerda por números crescentes a partir do número 2, como no exemplo abaixo:

#CPF

#1

#1

#1

#4

#4

#4

#7

#7

#7

#Multiplicador

#10

#9

#8

#7

#6

#5

#4

#3

#2

#Resultado

#10

#9

#8

#28

#24

#20

#28

#21

#14



#Em seguida somamos o resultado: 10+9+8+28+24+20+28+21+14 = 162

#Pegamos o resultado e dividimos por 11:  162 / 11 = 14 com resto 8

#Se o resto da divisão for menor que 2, então o dígito é igual a 0 (Zero).

#Se o resto da divisão for maior ou igual a 2, então o dígito verificador é igual a 11 menos o resto da divisão (11 - resto).

#No nosso exemplo temos que o resto é 8 então faremos 11-8 = 3. Logo o primeiro dígito verificador é 3. Então sabemos que o CPF deve ser:  111.444.777-3X

#Para  calcular o segundo dígito vamos usar o primeiro dígito já calculado. Vamos montar a mesma tabela de multiplicação usada no cálculo do primeiro dígito. Só que desta vez usaremos na segunda linha os valores 11,10,9,8,7,6,5,4,3,2 já que estamos incluindo mais um dígito no cálculo:

#CPF

#1

#1

#1

#4

#4

#4

#7

#7

#7

#3

#Multiplicador

#11

#10

#9

#8

#7

#6

#5

#4

#3

#2

#Resultado

#11

#10

#9

#32

#28

#24

#35

#28

#21

#6


#Somamos: 11 + 10 + 9 + 32 + 28 + 24 + 35 + 28 + 21 + 6 = 204

#Dividimos o total do somatório por 11 e consideramos o resto da divisão.

#204 / 11  =  18  e  resto 6



#Aplicamos a mesma regra que utilizamos para obter o primeiro dígito:

#Se o resto da divisão for menor que 2, então o dígito é igual a 0 (Zero).

#Se o resto da divisão for maior ou igual a 2, então o dígito é igual a 11 menos o resto da divisão (11 - resto).



#11-6 = 5, logo 5 é o nosso segundo dígito verificador e o CPF completo é:

#111.444.777-35



#O CPF de entrada deve ser considerado válido se os dígitos fornecidos pelo usuário forem os mesmos dígitos calculados através do processo acima.

#Exemplos válidos

#Exemplos inválidos

#545.315.761-52

#545.315.761-12

#473.063.662-70

#473.063.662-98

#775.682.566-77

#775.682.566-13


import re

def calcular_digito(cpf, multiplicadores):
    soma = sum(int(cpf[i]) * multiplicadores[i] for i in range(len(multiplicadores)))
    resto = soma % 11
    return '0' if resto < 2 else str(11 - resto)

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)  # Remove pontos e traço

    if len(cpf) != 11 or len(set(cpf)) == 1:
        return "Inválido"

    primeiro_digito = calcular_digito(cpf[:9], range(10, 1, -1))
    segundo_digito = calcular_digito(cpf[:9] + primeiro_digito, range(11, 1, -1))

    return "Válido" if cpf[-2:] == primeiro_digito + segundo_digito else "Inválido"

cpf = input("Digite um CPF no formato XXX.XXX.XXX-XX: ")
print(validar_cpf(cpf))
