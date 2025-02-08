'''
Escreva um programa, em que utilize a instrução while,
que apresente a tabuada do número solicitado
'''
while True:
    try:
        num = abs(int(input("Digite um número para a tabuada: ")))
        break
    except ValueError:
        print("Erro: Por favor, digite um número inteiro.")

i = 1
while i <= 10:
    print(f'{num} x {i} = {num * i}')
    i += 1
    
