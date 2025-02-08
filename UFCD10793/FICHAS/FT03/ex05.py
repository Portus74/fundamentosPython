'''Escreva um programa que verifique se um determinado número introduzido pelo utilizador é nulo, positivo ou negativo
'''
# Solicitar ao utilizador que introduza um número
num = input("Introduza um número: ")
# Verificar se o número é nulo, positivo ou negativo
if num == "0":
    print("O número é nulo.")
elif int(num) > 0:
    print("O número é positivo.")
else:
    print("O número é negativo.")