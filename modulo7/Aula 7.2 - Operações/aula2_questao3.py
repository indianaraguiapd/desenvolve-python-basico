#Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo (ou seja, lida da mesma forma de trás para frente). Ignore espaços em branco ou sinais de pontuação, e considere maiúsculas e minúsculas da mesma forma. Seu programa deve continuar rodando até que o usuário digite "Fim".

#Digite uma frase (digite "fim" para encerrar): Radar

#"Radar" é palíndromo

#Digite uma frase (digite "fim" para encerrar): Bom dia!

#"Bom dia!" não é palíndromo

#Digite uma frase (digite "fim" para encerrar): Ame o poema

#"Ame o poema" é palíndromo

#Digite uma frase (digite "fim" para encerrar): A Daniela ama a lei? Nada!

#"A Daniela ama a lei? Nada!" é palíndromo

#Digite uma frase (digite "fim" para encerrar): fim

def eh_palindromo(frase):
    # Remove espaços, pontuação e converte para minúsculas
    caracteres = ''.join(c.lower() for c in frase if c.isalnum())
    # Compara a string com sua versão invertida
    return caracteres == caracteres[::-1]

while True:
    entrada = input('Digite uma frase (digite "fim" para encerrar): ')

    if entrada.lower() == 'fim':
        break

    if eh_palindromo(entrada):
        print(f'"{entrada}" é palíndromo')
    else:
        print(f'"{entrada}" não é palíndromo')