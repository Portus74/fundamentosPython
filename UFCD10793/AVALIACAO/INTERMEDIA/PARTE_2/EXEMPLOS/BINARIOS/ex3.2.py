'''
Ler um ficheiro binário em blocos (eficiente para ficheiros grandes)
'''

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/BINARIOS/AlbertEinstein4Kids.mp4'
with open(caminho_ficheiro, 'rb') as ficheiro:
    while chunk := ficheiro.read(4096):
    # Processamento do chunk
        print(chunk[:10])