try:
    numero = int(input("Digite um número: "))
    print("O dobro do númerro é:", numero * 2)
except ValueError:
    print("Erro: Digite apenas números inteiros.")
