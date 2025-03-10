#Tratamento de Erros em PYTHON
try:
    numero = int(input("Digite um número: "))
    print("O dobro do número é: ", numero * 2)
except ValueError:
    print("Erro: Digite apenas números inteiros.")