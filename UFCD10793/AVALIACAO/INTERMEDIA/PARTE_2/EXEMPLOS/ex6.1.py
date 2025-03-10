'''
Evitar erros ao tentar abrir ficheiros inexistentes:
'''
import os

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/exemplo.txt'


if os.path.exists(caminho_ficheiro):
    with open(caminho_ficheiro, "r") as ficheiro:
        print(ficheiro.read())
else:
    print("Erro: O ficheiro não foi encontrado.")