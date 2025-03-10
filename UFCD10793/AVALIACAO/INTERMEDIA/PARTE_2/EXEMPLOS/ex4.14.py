# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/exemplo.txt'

with open(caminho_ficheiro, "w") as ficheiro:
    ficheiro.write("Esta é a nova primeira linha.")
    ficheiro.write("Segunda linha do ficheiro.")