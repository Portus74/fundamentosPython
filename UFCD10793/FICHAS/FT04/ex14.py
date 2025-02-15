'''
Elabora um programa que pede ao utilizador para inserir
dois números inteiros. O programa deve escrever todos
os números inteiros entre os limites por odem decrescente.
Utiliza o ciclo for.
'''

import os
os.system('cls' if os.name == 'nt' else 'clear')

while True:
    try:
        n1 = abs(int(input("Introduza 1º número inteiro: ")))
        n2 = abs(int(input("Introduza 2º número inteiro: ")))
        break
    except ValueError:
        print("Erro: Por favor, introduza um número inteiro.")

menor = min(n1, n2)
maior = max(n1, n2)
print(f'\nNúmeros inteiros entre {menor} e {maior} em ordem crescente')
for i in range(menor, maior + 1):
    print(i)

print(f'\nNúmeros inteiros entre {menor} e {maior} em ordem decrescente')

#Podemos criar uma lista de valores a ser percorrido pelo ciclo for
x = range(maior, menor - 1, -1)
for i in x:
    print(i) 