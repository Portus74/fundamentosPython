'''
Verificar se o ficheiro JSON existe antes de o abrir
'''

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/JSON/dadosListas.json'

import os
if os.path.exists(caminho_ficheiro):
    with open(caminho_ficheiro, "r") as ficheiro:
        print(ficheiro.read())
else:
    print(f"O ficheiro {caminho_ficheiro} não encontrado.")
    