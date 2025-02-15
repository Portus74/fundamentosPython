'''
Reescreve o programa anterior de forma a apresentar
a tabuada de qualquer número introduzido pelo utilizador
'''

import os
os.system('cls' if os.name == 'nt' else 'clear')

while True:
    try:
        n = abs(int(input("Introduza um número para a tabuada: ")))
        break
    except ValueError:
        print("Erro: Por favor, introduza um número inteiro.")
        
i = 1
while i <= 10:
    print(f'')
    print(f'{i} x {n} = {i * n}')
    i += 1