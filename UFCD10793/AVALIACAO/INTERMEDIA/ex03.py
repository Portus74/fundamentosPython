'''
Exemplos parra cada exceção

i. Exemplo   de ValueErrornt
'''
# i. Exemplo de ValueError
try:
    idade = int(input("Digite sua idade: "))
except ValueError:
    print("Erro: Dgiite um inteiro válido.")
    
# i. Exemplo de ZeroDivisionError:
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")

#iii. Exemplo de FileNotFoundError:
try:
    with open("arquivo_inexistente.txt", "r") as file:
        conteudo = file.read()
except FileNotFoundError:
        print("Erro: O ficheiro não foi encontrado.")