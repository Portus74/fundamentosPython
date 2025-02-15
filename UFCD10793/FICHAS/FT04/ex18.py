'''
Elabore um programa que calcule e mostre no ecrã os números pares entre 1 e 200
'''

min = 1
max = 201

x = range(min, max, 1)

for i in x:
    if i % 2 == 0:
        print(f'Número par: {i}')