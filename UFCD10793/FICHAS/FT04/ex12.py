'''
Escreve um programa que calcule e escreva o resultado
do fatorial de um número inteiro positivo N
sabendo que n! = 1*2*3*...*n
'''

import os
os.system('cls' if os.name == 'nt' else 'clear')

while True:
    try:
        n = abs(int(input("Introduza um número inteiro: ")))
        break
    except ValueError:
        print("Erro: Por favor, introduza um número inteiro.")
        
fatorial = 1
i = 1
while i <= n:
    fatorial *= i
    i += 1
    
print(f'Fatorial do número {n} = {fatorial}')
