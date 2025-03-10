'''
Leitura de um ficheiro CSV
'''

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/CSV/dados.csv'

import csv
with open(caminho_ficheiro, newline='', encoding="utf-8") as ficheiro:
    leitor = csv.reader(ficheiro)
    for linha in leitor:
        print(linha)#m ficheiro CSV