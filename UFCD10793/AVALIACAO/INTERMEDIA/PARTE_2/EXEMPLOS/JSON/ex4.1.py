'''
Ler um ficheiro JSON e convertê-lo num dicionário
'''

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/JSON/dados.json'

import json
with open(caminho_ficheiro, "r", encoding="utf-8") as ficheiro:
    dados = json.load(ficheiro)

print(dados["nome"])