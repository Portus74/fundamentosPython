'''
Copiar ficheiro binário
'''

# Localização e ficheiro
caminho_ficheiroOrigem = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/BINARIOS/Logo-EISNT-01.png'

caminho_ficheiroDestino = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/BINARIOS/Logo-EINST-02.png'

# Abrir o ficheiro em modo de escrita
with open(caminho_ficheiroOrigem, "rb") as origem:
    with open(caminho_ficheiroDestino, "wb") as destino:
        # Ler o ficheiro e copiar para o destino
        destino.write(origem.read())
        print("Ficheiro copiado com sucesso!")

        