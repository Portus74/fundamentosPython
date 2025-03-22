# Definição do texto
txt = """Python é uma linguagem de programação
de alto nível, interpretada de script, imperativa, orientada a objetos,
funcional, de tipagem dinâmica e forte."""

# a. Imprimir texto em maiúsculas
print("Texto em maiúsculas:")
print(txt.upper())
print()

# b. Verificar se palavra existe no texto usando comprehension
palavra = input("Digite uma palavra para procurar no texto: ")
# List comprehension para encontrar todas as palavras que correspondem à busca
palavras_encontradas = [p for p in txt.lower().split() if palavra.lower() in p]
print(f"A palavra '{palavra}' {'ESTÁ' if palavras_encontradas else 'NÃO está'} presente no texto.")
print()

# c. Contar ocorrências da letra 'O' usando comprehension
# Usando sum com generator expression
contagem_o = sum(1 for letra in txt.lower() if letra == 'o')
print(f"A letra 'O' aparece {contagem_o} vezes no texto.")
print()

# d. Substituir 'P' por '_' usando comprehension
# Usando join com generator expression
novo_texto = ''.join('_' if letra.lower() == 'p' else letra for letra in txt)
print("Texto com 'P' substituído por '_':")
print(novo_texto)

# Bônus: podemos também criar uma lista de todas as palavras usando list comprehension
palavras = [palavra for palavra in txt.split()]
print("\nLista de todas as palavras do texto:")
print(palavras)

# Bônus: encontrar todas as palavras que começam com vogais
vogais = 'aeiouAEIOU'
palavras_com_vogais = [palavra for palavra in txt.split() if palavra[0] in vogais]
print("\nPalavras que começam com vogais:")
print(palavras_com_vogais)