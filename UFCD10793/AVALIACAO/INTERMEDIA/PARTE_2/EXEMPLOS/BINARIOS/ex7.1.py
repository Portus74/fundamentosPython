'''
Verificar se um ficheiro binário existe
'''

import os

# Localização e ficheiro
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/BINARIOS/Logo-EISNT-01.png'

if os.path.exists(caminho_ficheiro):
    with open(caminho_ficheiro, 'rb') as ficheiro:
        print("Ficheiro encontrado.")
else:
    print("Erro: O ficheiro não existe")