# Definição do texto
txt = """Python é uma linguagem de programação
de alto nível, interpretada de script, imperativa, orientada a objetos,
funcional, de tipagem dinâmica e forte."""

# a. Imprimir texto em maiúsculas
print("Texto em maiúsculas:")
print(txt.upper())
print()

# b. Verificar se palavra existe no texto
palavra = input("Digite uma palavra para procurar no texto: ")
if palavra.lower() in txt.lower():  # converte ambos para minúsculas para fazer busca case-insensitive
    print(f"A palavra '{palavra}' ESTÁ presente no texto.")
else:
    print(f"A palavra '{palavra}' NÃO está presente no texto.")
print()

# c. Contar ocorrências da letra 'O'
# Considerando tanto 'o' minúsculo quanto maiúsculo
contagem_o = txt.lower().count('o')
print(f"A letra 'O' aparece {contagem_o} vezes no texto.")
print()

# d. Substituir 'P' por '_'
# Considerando tanto 'p' minúsculo quanto maiúsculo
novo_texto = txt.replace('P', '_').replace('p', '_')
print("Texto com 'P' substituído por '_':")
print(novo_texto)