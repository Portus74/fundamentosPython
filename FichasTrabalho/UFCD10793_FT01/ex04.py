'''Escreve um programa que calcule o volume de uma esfera.
O valor do raio deverá ser introduzido pelo utilizador'''

#importar a biblioteca
import math

print("Calcular o volume de uma esfera")
raio = int(input("Digite o raio: "))

volume = (4/3) * math.pi * (raio ** 3)
print("O volume da esfera é: ", round(volume, 2))
