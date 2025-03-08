'''
Elabora uma script em python que peça ao utilizador dois números
e devolva a divisão do primeiro número introduzido pelo seguinte.
Trate erros como divisão por zero e valores inválidos.
'''
def realizar_divisao(numerador, denominador):
    """
    Função que realiza a divisão entre dois números
    Retorna o resultado da divisão
    """
    return numerador / denominador

def obter_numero(mensagem):
    """
    Função que obtém e valida um número do utilizador
    Retorna o número convertido para float
    """
    while True:
        try:
            numero = input(mensagem)
            # Tenta converter para float
            return float(numero)
        except ValueError:
            print("Erro: Por favor, introduza um número válido!")

def main():
    print("=== Programa de Divisão ===")

    while True:
        try:
            # Obter os números do utilizador
            numerador = obter_numero("Introduza o primeiro número (numerador): ")
            denominador = obter_numero("Introduza o segundo número (denominador): ")

            # Verificar divisão por zero
            if denominador == 0:
                raise ZeroDivisionError("Não é possível dividir por zero!")

            # Realizar a divisão
            resultado = realizar_divisao(numerador, denominador)

            # Mostrar o resultado
            print(f"\nResultado da divisão:")
            print(f"{numerador} ÷ {denominador} = {resultado:.2f}")
            break  # Sai do loop se tudo correr bem

        except ZeroDivisionError as zde:
            print(f"\nErro: {zde}")

        except Exception as e:
            print(f"\nErro inesperado: {e}")

        finally:
            # Pergunta se quer tentar novamente em caso de erro
            if 'resultado' not in locals():
                resposta = input("\nDeseja tentar novamente? (s/n): ").lower()
                if resposta != 's':
                    print("Programa terminado.")
                    break

if __name__ == "__main__":
    main()