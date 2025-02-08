'''Escreva um programa que receba três números reais e indique qual o maior dos três números'''

numero1 = float(input("Insira o número 1 de 3:"))
numero2 = float(input("Insira o número 2 de 3:"))
numero3 = float(input("Insira o número 3 de 3:"))
if numero1 > numero2 and numero1 > numero3:
    maior = numero1
elif numero2 > numero1 and numero2 > numero3:
    maior = numero2
else:
    maior = numero3
print(f"O maior número é {maior}")
print(f"O maior número é {max([numero1,numero2,numero3])}")

    