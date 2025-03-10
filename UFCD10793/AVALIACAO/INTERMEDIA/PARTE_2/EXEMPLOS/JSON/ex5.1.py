'''
Criar e escrever num ficheiro JSON
'''

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/JSON/dadosCriados.json'

import json

dados = {
    "nome": "João",
    "idade": 25,
    "cidade": "Lisboa"
}

with open(caminho_ficheiro, "w", encoding="utf-8") as ficheiro:
    json.dump(dados, ficheiro, indent=4)
