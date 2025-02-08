'''utilizar o try except e pede um número inteiro e enquanto o número não for inteiro pede novamente'''

while True:
    try:
        num = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("Número inválido. Por favor, digite um número inteiro.")
        



