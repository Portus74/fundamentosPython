#Criar um programa que escreva três linhas num ficheiro novo.

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/novo_ficheiro.txt'

# Abrir o ficheiro no modo de adição e adiciona uma nova linha
with open(caminho_ficheiro, "a", encoding="utf-8") as ficheiro:
    ficheiro.write("Linha adicional\n")  # Adiciona quebra de linha
    
print("Linha adicionada com sucesso!")
