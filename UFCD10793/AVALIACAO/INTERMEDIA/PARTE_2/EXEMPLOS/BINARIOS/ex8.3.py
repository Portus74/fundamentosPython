'''
Garantir a integridade dos dados ao copiar ficheiros
'''

import hashlib

# Localização e ficheiro
caminho_ficheiroOrigem = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/BINARIOS/Logo-EISNT-01.png'

caminho_ficheiroDestino = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/BINARIOS/Logo-EISNT-02.png'

def calcular_hash(ficheiro):
    hash_md5 = hashlib.md5()
    with open(ficheiro, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
        
if calcular_hash(caminho_ficheiroOrigem) == calcular_hash(caminho_ficheiroDestino):
    print("Os ficheiros são idênticos")
else:
    print("Os ficheiros são diferentes")
    