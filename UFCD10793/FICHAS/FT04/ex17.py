'''
Escreva um programa que peça ao utilizador 20 números reais e no final mostre a soma
e a média dos números introduzidos
'''

    
soma = 0
nVezes = 5
x = range(1, nVezes, 1)
for n in x:
    numero = float(input("\nInsira um número:"))
    soma += numero

print(f'Soma final = {soma}, média final = {soma / nVezes} ')
