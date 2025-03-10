# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/exemplo.txt'

with open("exemplo.txt", "a") as ficheiro:
    ficheiro.write("Nova linha adicionada.")