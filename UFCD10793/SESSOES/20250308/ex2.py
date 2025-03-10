import string

def contar_palavras(texto):
    """
    Conta o número de palavras em um texto, removendo sinais de pontuação.

    Args:
      texto: A string representando o texto.

    Returns:
      O número de palavras no texto após a remoção da pontuação.
    """

    # Remove a pontuação do texto
    pontuacao = string.punctuation  # Obtém todos os sinais de pontuação
    for sinal in pontuacao:  # Itera sobre cada sinal de pontuação
        texto = texto.replace(sinal, "")  # Substitui cada sinal por uma string vazia

    # Divide o texto em palavras
    palavras = texto.split()

    # Retorna o número de palavras
    return len(palavras)


# Obtém o texto do usuário
texto = input("Digite um texto: ")

# Conta o número de palavras
numero_de_palavras = contar_palavras(texto)

# Imprime o resultado
print("O número de palavras no texto é:", numero_de_palavras)