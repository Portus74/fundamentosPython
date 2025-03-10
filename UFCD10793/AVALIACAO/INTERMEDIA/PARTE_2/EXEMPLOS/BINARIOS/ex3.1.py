'''
Ler um ficheiro binário completamente
'''

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/BINARIOS/Logo-EISNT-01.png'
with open(caminho_ficheiro, 'rb') as ficheiro:
    # Ler o ficheiro binário
    conteudo_ficheiro = ficheiro.read()
    print(conteudo_ficheiro[:20])