'''
Escrita num ficheiro CSV - O código seguinte cria um ficheiro CSV com duas colunas (Nome, Idade).
'''

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/CSV/dadosCriados.csv'

import csv
dados = [["Nome", "Idade"], ["João", 25], ["Ana", 30]]
with open(caminho_ficheiro, "w", newline='', encoding="utf-8") as ficheiro:
    escritor = csv.writer(ficheiro)
    escritor.writerows(dados)