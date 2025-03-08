'''
Elabora uma script em python que peça ao utilizador um número
e some todos os números de 1 até esse mesmo número.
Deves utilizar o tratamento de erros.
'''

print("=== Programa de Soma de Números ===")

while True:
    try:
        # Pedir um número ao utilizador
        numero = int(input("Digite um número inteiro positivo: "))

        # Verificar se o número é positivo
        if numero <= 0:
            print("Erro: O número deve ser positivo!")
        else:
            # Calcular a soma usando um loop for
            soma = 0
            for i in range(1, numero + 1):
                soma = soma + i

            # Mostrar o resultado
            print(f"\nA soma de todos os números de 1 até {numero} é: {soma}")

            # Mostrar os números que foram somados
            print("\nNúmeros somados:", end=" ")
            for i in range(1, numero + 1):
                if i < numero:
                    print(i, end=" + ")
                else:
                    print(i, end=" = ")
            print(soma)
            break  # Sai do programa se tudo correr bem

    except ValueError:
        print("Erro: Por favor, digite apenas números inteiros!")

    # Perguntar se quer tentar novamente
    continuar = input("\nQuer tentar novamente? (s/n): ")
    if continuar.lower() != 's':
        print("Programa terminado.")
        break