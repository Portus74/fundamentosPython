'''
Elabora uma script em python que peça ao utilizador um número
e some todos os números de 1 até esse mesmo número.
Deves utilizar o tratamento de erros.
'''

def somar_ate_n(numero):
    """
    Função que soma todos os números de 1 até ao número fornecido
    Retorna a soma e uma lista com todos os números utilizados
    """
    numeros = list(range(1, numero + 1))
    soma = sum(numeros)
    return soma, numeros

def main():
    while True:
        try:
            # Solicitar input ao utilizador
            numero = input("Por favor, introduza um número inteiro positivo: ")

            # Converter input para inteiro e verificar se é positivo
            numero = int(numero)
            if numero <= 0:
                raise ValueError("O número deve ser positivo!")

            # Calcular a soma
            soma, numeros = somar_ate_n(numero)

            # Mostrar resultados
            print("\nResultados:")
            print(f"Números somados: {' + '.join(map(str, numeros))} = {soma}")
            print(f"A soma de todos os números de 1 até {numero} é: {soma}")
            break  # Sai do loop se tudo correr bem

        except ValueError as ve:
            # Captura erro de conversão para inteiro ou número não positivo
            if str(ve) == "O número deve ser positivo!":
                print(f"\nErro: {ve}")
            else:
                print("\nErro: Por favor, introduza apenas números inteiros!")

        except Exception as e:
            # Captura outros erros inesperados
            print(f"\nErro inesperado: {e}")

        finally:
            # Pergunta se quer tentar novamente em caso de erro
            if 'soma' not in locals():
                resposta = input("\nDeseja tentar novamente? (s/n): ").lower()
                if resposta != 's':
                    print("Programa terminado.")
                    break

if __name__ == "__main__":
    print("=== Programa de Soma de Números ===")
    main()