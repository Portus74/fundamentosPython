# Programa 1: Gerar o CSV
import csv
import random

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/potencias.csv'

def gerar_csv_potencias():
    with open(caminho_ficheiro, 'w', newline='') as file:
        writer = csv.writer(file)

        # Escrever cabeçalho
        writer.writerow(['Base', 'Expoente', 'Resultado', 'Probabilidade', 'Classificação'])

        # Gerar dados
        for base in range(1, 11):
            for expoente in range(1, 5):
                resultado = base ** expoente
                probabilidade = round(random.random(), 3)

                # Determinar classificação
                if probabilidade > 0.66:
                    classificacao = "Alta"
                elif probabilidade > 0.33:
                    classificacao = "Média"
                else:
                    classificacao = "Baixa"

                writer.writerow([base, expoente, resultado, probabilidade, classificacao])

# Gerar o CSV
gerar_csv_potencias()
print("Ficheiro 'potencias.csv' criado com sucesso!\n")
