'''
O método `chunking` permite ler ficheiros grandes
sem sobrecarregar a RAM 
(ler e escrever em partes - chuncks).
'''

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/grande_ficheiro.txt'

with open(caminho_ficheiro, "r") as ficheiro: 
    while chunk := ficheiro.read(1024):#Lê 1024 bytes de cada vez 
        print(chunk)