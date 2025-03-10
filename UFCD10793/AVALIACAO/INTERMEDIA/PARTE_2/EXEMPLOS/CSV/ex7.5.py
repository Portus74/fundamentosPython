'''
Escrever ficheiros CSV formatados com DictWriter
'''

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/CSV/dadosFormatados.csv'

import csv
dados = [
{"Nome": "João", "Idade": 25, "Cidade": "Lisboa"},
{"Nome": "Maria", "Idade": 30, "Cidade": "Porto"}
]
with open(caminho_ficheiro, "w", newline='', encoding="utf-8") as ficheiro:
    campos = ["Nome", "Idade", "Cidade"]
    escritor = csv.DictWriter(ficheiro, fieldnames=campos)
    escritor.writeheader() # Escreve os cabeçalhos
    escritor.writerows(dados) # Escreve os dados