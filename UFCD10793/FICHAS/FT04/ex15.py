'''
Escreve um programa que mostre no ecrã os 20 primeiros múltiplos de 5
'''

x = range(1, 21, 1)
print('\nApresentação de primeiros 20 múltiplos de 5')
for i in x:
    print(f'{i * 5}')