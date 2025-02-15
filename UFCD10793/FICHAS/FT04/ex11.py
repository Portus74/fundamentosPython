'''
Escreve um programa que calcule a soma e o produto
dos N primeiros números naturais
'''

import os
os.system('cls' if os.name == 'nt' else 'clear')

while True:
    try:
        n = abs(int(input("Introduza um número inteiro: ")))
        break
    except ValueError:
        print("Erro: Por favor, introduza um número inteiro.")
        
i = 1
soma = 0
produto = 1
while i <= n:
    #print(f'{i} x {n} = {i * n}')
    i += 1
    soma += i
    produto *= i
    
print(f'Soma final = {soma}')
print(f'Produto final = {produto}')