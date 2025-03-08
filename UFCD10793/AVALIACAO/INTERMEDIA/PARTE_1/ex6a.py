'''
Elabora uma script em python que peça ao utilizador dois números
e devolva a divisão do primeiro número introduzido pelo seguinte.

Trate erros como divisão por zero e valores inválidos.
'''
print("=== Programa de Divisão ===")

while True:
    try:
        # Pedir os números ao utilizador
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        # Verificar se o segundo número é zero
        if numero2 == 0:
            print("Erro: Não é possível dividir por zero!")
        else:
            # Realizar a divisão
            resultado = numero1 / numero2
            print(f"\nO resultado de {numero1} dividido por {numero2} é: {resultado}")
            break  # Sai do programa se tudo correr bem

    except ValueError:
        print("Erro: Por favor, digite apenas números!")

    # Perguntar se quer tentar novamente
    continuar = input("\nQuer tentar novamente? (s/n): ")
    if continuar.lower() != 's':
        print("Programa terminado.")
        break