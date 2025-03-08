'''
2. Lista de Exceções específicas em Python
'''

# i. Value Error: Erro de conversão de tipo de dados
try:
    numero = int(input("Digite um número intiero: "))
    print("Número inserido: ", numero)
except ValueError:
    print("Erro: O valor deve ser um númeror inteiro.")

# ii. ZeroDivisionError: Tentativa de divisão por zero
try:
    a = int(input("Digiteo  numerdador: "))
    b = int(input("Digite o denominador: "))
    resultado = a / b
    print("O resultado é: ", resultado)
except ZeroDivisionError:
    print("Erro: Naõ é possível dividir por zero.")
# iii. FileNotFoundError: O ficheiro solicitado não foi encontrado
# iv. IndexError: Tentativa de acessar um índice inválido numa lista
# v. KeyError: Tentativa de acessar uma chave inexistente num dicionário
# vi. TypeError: Operação inválida entre tipos de dados incompatíveis
# vii. NameError: Uso de uma variável que não foi definida
# viii. AttributeError: Tentativa de acessar im atributo inexistente de um objeto
# ix. IOError: Erro ao lidar com operações de entrada/saída
# X. RuntimeError: Erro inesperado em tempo de execução