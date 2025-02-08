'''
Escreva um programa que solicite ao utilizador dois números inteiros
a operação matemática a ser realizada (+, -, * e /)

Utilize a estrutura match...case para executar a operação escolhida
e devolver o resultado
'''

operador = input("Escolha a operação (+, -, *, /): ")

while True:
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        break
    except ValueError:
        print("Erro: Por favor, introduza valores numéricos")


match operador:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Operação impossível de realizar")
    case _:
        print("Operador inválido")  # Adicione essa linha para tratar o caso