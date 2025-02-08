'''
Fazer um programa para ler quatro números inteiros e positivos,
calcular e devolver a sua média
'''
# Ler quatro números inteiros e positivos
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
num4 = int(input("Digite o quarto número: "))
# Calcular a média
media = (num1 + num2 + num3 + num4) / 4
# Devolver a média
print("A média dos números é: ", media)

soma = 0
i = 1
while i <= 4:
    while True:
        try:
            # Ler um número inteiros e positivos
            num = abs(int(input(f"Digite um número {i}: ")))
            break
        except ValueError:
            print("Número inválido. Por favor, digite um número inteiro e positivo.")
    soma += num
    i += 1

print(f"A média é {soma / 4}")
