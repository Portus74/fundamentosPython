'''
Elabora um programa para somar todos os valores entre
10 e 100 (inclusive) e apresentar os valores no ecrã
'''

import os
os.system('cls' if os.name == 'nt' else 'clear')

'''
while True:
    try:
        n = abs(int(input("Introduza um número inteiro: ")))
        break
    except ValueError:
        print("Erro: Por favor, introduza um número inteiro.")
'''
        
min = 10
max = 100
soma = 0

while min <= max:
    soma += min
    min += 1

print(f'Soma final = {soma}')
