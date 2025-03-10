'''
Ler e Escrever binários com bytearray
'''

# Localização e ficheiro
caminho_ficheiroOrigem = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/BINARIOS/ficheiro.bin'

caminho_ficheiroDestino = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/BINARIOS/dados_modificados.bin'

# Abrir o ficheiro em modo de escrita
with open(caminho_ficheiroOrigem, "rb") as ficheiro:
    conteudo = bytearray(ficheiro.read())

conteudo[0] = 255

with open(caminho_ficheiroDestino, "wb") as ficheiro:
    ficheiro.write(conteudo)
    