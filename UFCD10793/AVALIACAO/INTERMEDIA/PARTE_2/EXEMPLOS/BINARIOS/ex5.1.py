'''
Acrescentar dados a um ficheiro
'''

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/BINARIOS/ficheiro.bin'

dados_extra = "\nNova informação binária.".encode('utf-8')

# Abrir o ficheiro em modo de escrita
with open(caminho_ficheiro, "ab") as ficheiro:
    ficheiro.write(dados_extra)