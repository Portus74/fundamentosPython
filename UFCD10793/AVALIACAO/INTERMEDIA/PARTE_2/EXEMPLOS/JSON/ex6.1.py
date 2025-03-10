'''
Adicionar novos dados a um ficheiro JSON
'''

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/JSON/dados.json'

import json

#Abrir o ficheiro e carregar os dados
with open(caminho_ficheiro, "r", encoding="utf-8") as ficheiro:
    dados = json.load(ficheiro)

#Modificar os dados
dados['email'] = 'joao@email.com'

#Gravar novamente no ficheiro JSON
with open(caminho_ficheiro, "w", encoding="utf-8") as ficheiro:
    json.dump(dados, ficheiro, indent=4)

