'''
Ler um ficheiro CSV com cabeçalhos e converter para dicionário
'''

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/CSV/dados.csv'

import csv
with open(caminho_ficheiro, newline='', encoding="utf-8") as ficheiro:
    leitor = csv.DictReader(ficheiro) # Converte cada linha num dicionário
    for linha in leitor:
        print(linha["Nome"], "-", linha["Idade"])