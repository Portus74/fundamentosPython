'''
Criar e escrever num ficheiro binário
'''

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/BINARIOS/ficheiro.bin'

dados = "Isto é apenas um exemplo de ficheiro binário".encode('utf-8')

# Abrir o ficheiro em modo de escrita
with open(caminho_ficheiro, "wb") as ficheiro:
    ficheiro.write(dados)