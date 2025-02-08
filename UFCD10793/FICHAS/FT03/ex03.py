'''Escreve um programa que solicite um número inteiro ao utilizador e verifique se o mesmo é par ou ímpar. A mensagem no ecrã deverá ter o seguinte formato:
O número [número] é [par/ímpar]'''
# Solicita um número ao utilizador
numero = int(input("Introduza um número: "))
# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
    
