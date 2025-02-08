'''
Implemente uma calculadora simples com as operações aritméticas básicas.
O utilizador deverá especificar a operação desejada (+,-,*,/)
e, em seguida, inserir dois valores.

Caso, o utilizador escolha divisão e insira como valor do denominar 0 
mostra uma mensagem personalizada. 

Para os restantes casos, mostra no ecrã o resultado da operação desejada.
'''
# Função para calcular a operação desejada
def calcular(operador, valor1, valor2):
    if operador == '+':
        return valor1 + valor2
    elif operador == '-':
        return valor1 - valor2
    elif operador == '*':
        return valor1 * valor2
    elif operador == '/':
        if valor2 == 0:
            return "Não é possível dividir por zero!"
        else:
            return valor1 / valor2

# Função principal
def main():
    # Solicitação do operador
    operador = input("Escolha a operação (+, -, *, /): ")
    valor1 = float(input("Insira o primeiro valor:"))
    valor2 = float(input("Insira o segundo valor: "))
    
    calcular(operador, valor1, valor2)
    
    print(f"O resultado da operação {operador} é: {calcular(operador, valor1, valor2)}")

main()