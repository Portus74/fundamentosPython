'''
Acrescentar dados a um ficheiro CSV existente
'''

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/CSV/dadosCriados.csv'

import csv
novos_dados = [
["Carlos", 35, "Braga"],
["Ana", 40, "Faro"]
]
with open(caminho_ficheiro, "a", newline='', encoding="utf-8") as ficheiro:
    escritor = csv.writer(ficheiro)
    escritor.writerows(novos_dados) # Adiciona novas linhas sem apagar as existentes