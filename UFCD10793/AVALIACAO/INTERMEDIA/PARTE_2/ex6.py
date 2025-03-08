import csv
# Localização e ficheiro potencias.csv
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/potencias.csv'

def ler_csv_potencias():
    print("Lendo o ficheiro 'potencias.csv':")
    print("-" * 70)

    try:
        with open(caminho_ficheiro, 'r') as file:
            reader = csv.reader(file)

            # Ler e mostrar cabeçalho
            cabecalho = next(reader)
            print(f"{cabecalho[0]:<6} {cabecalho[1]:<10} {cabecalho[2]:<10} {cabecalho[3]:<14} {cabecalho[4]}")
            print("-" * 70)

            # Ler e mostrar cada linha
            for linha in reader:
                print(f"{linha[0]:<6} {linha[1]:<10} {linha[2]:<10} {linha[3]:<14} {linha[4]}")

    except FileNotFoundError:
        print("Erro: Ficheiro 'potencias.csv' não encontrado!")
    except Exception as e:
        print(f"Erro ao ler o ficheiro: {e}")

# Executar a leitura
ler_csv_potencias()