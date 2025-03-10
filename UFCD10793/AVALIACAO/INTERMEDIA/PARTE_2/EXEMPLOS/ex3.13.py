# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/exemplo.txt'

with open(caminho_ficheiro, "r") as ficheiro:
    linhas = ficheiro.readlines() 
    for linha in linhas: 
        print(linha.strip())