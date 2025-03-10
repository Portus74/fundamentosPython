'''
Prevenir falhas com tre-except - garante robustez contra falhas
'''

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/EXEMPLOS/exemplo.txt'


try:
    with open(caminho_ficheiro, "r") as ficheiro:
        print(ficheiro.read())
except FileNotFoundError:
    print("Erro: O ficheiro não existe.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")