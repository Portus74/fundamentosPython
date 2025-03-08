#Criar um programa que escreva três linhas num ficheiro novo.

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/novo_ficheiro.txt'

# Criar e escrever no ficheiro "novo_ficheiro.txt"
with open(caminho_ficheiro, "w", encoding="utf-8") as ficheiro:
    ficheiro.write("Linha 1\n")  # Adiciona quebra de linha
    ficheiro.write("Linha 2\n")  # Adiciona quebra de linha
    ficheiro.write("Linha 3\n")  # Adiciona quebra de linha

print("Ficheiro criado com sucesso!")
