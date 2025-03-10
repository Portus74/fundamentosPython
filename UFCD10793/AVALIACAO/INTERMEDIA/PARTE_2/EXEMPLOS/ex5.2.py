'''
mmap permite mapear ficheiros diretamente para a memória
(altamente eficiente para ficheiros grandes.
'''

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/grande_ficheiro.txt'

import mmap
with open("grande_ficheiro.txt", "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0)
    print(mm.readline())
    mm.close()