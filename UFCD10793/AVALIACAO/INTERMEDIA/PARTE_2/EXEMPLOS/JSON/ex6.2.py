'''
Trabalhar com Listas dentro de JSON
'''

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/JSON/dadosListas.json'

import json

dados = {
    "nome": "João",
    "contactos": ["joao@email.com", "912345678"]
}

with open(caminho_ficheiro, 'w', encoding="utf-8") as ficheiro:
    json.dump(dados, ficheiro, indent=4)

#Ler o ficheiro e exibi a lista de contactos
with open(caminho_ficheiro, 'r', encoding="utf-8") as ficheiro:
    dados_lidos = json.load(ficheiro)
    print(dados_lidos["contactos"])
