'''
Escreva um programa em python que, dada uma sequencia de números inteiros
(todos fornecidos na mesma liunha, separados por espaços),
imprima a média desses numeros
'''
def calcular_media(sequencia):
  """
  Calcula a média de uma sequência de números inteiros fornecida como string.

  Args:
    sequencia: Uma string contendo números inteiros separados por espaços.

  Returns:
    A média dos números na sequência, ou None se a sequência estiver vazia ou contiver dados inválidos.
  """
  try:
    numeros = [int(x) for x in sequencia.split()]
    if not numeros:  # Verifica se a lista está vazia
      return None
    return sum(numeros) / len(numeros)
  except ValueError:
    return None  # Retorna None se houver erro de conversão (não inteiro)


# Obtém a sequência de números do usuário
entrada = input("Digite uma sequência de números inteiros separados por espaços: ")

# Calcula a média
media = calcular_media(entrada)

# Imprime o resultado
if media is not None:
  print("A média dos números é:", media)
else:
  print("Entrada inválida. Certifique-se de fornecer apenas números inteiros separados por espaços.")