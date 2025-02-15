'''
Escreva um programa que peça ao utilizador números entre 0..10.
Se o utilizador inserir um número fora desse intervalo o programa
deverá finalizar com uma mensagem personalizada.
'''

import os
os.system('cls' if os.name == 'nt' else 'clear')

'''''
n = 0
x = range(1, 11)
while n in x:
    n = abs(int(input("Introduza um número inteiro entre [0..10]: ")))

'''

while True:
    try:
        numero = int(input("Insira um número entre 0 e 10: "))

        if 0 <= numero <= 10:
            print("Número válido:", numero)
        else:
            print("Erro: O número", numero, "está fora do intervalo permitido (0 a 10).")
            break  # Sai do loop (finaliza o programa)

    except ValueError:
        print("Erro: Por favor, insira um número inteiro válido.")
        break # Sai do loop se a entrada não for um inteiro.