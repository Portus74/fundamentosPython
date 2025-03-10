'''
Tratar erros ao ler ficheiros JSON
'''

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/JSON/dadosListas.json'

import json
try:
    # Ler ficheiro JSON
    with open(caminho_ficheiro, "r", encoding="utf-8") as ficheiro:
        dados = json.load(ficheiro)
except FileNotFoundError:
    print(f'O ficheiro {caminho_ficheiro} não existe')
except json.JSONDecodeError:
    print(f'Erro: O ficheiro {caminho_ficheiro} está mal formatado.')
except Exception as e:
    print(f'Erro Inesperado: {e}')
