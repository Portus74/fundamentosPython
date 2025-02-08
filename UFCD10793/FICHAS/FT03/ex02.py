'''Implementa um programa que leia dois números e indique se estes são iguais ou diferentes
'''
# Ler dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
# Comparar os números
if num1 == num2:
    print("Os números são iguais")
elif num1 >= num2:
    print("O primeiro número é maior ou igual ao segundo")
else:
    print("O primeiro número é menor que o segundo")

    