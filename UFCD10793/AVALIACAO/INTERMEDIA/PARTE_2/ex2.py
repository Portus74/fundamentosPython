#Criar um programa que leia um ficheiro de texto e exibir o seu conteúdo
#O programa deve ler o ficheiro e exibir o seu conteúdo na tela
#O programa deve verificar se o ficheiro existe antes de tentar abrir-lo
import os
import sys

# Localização e ficheiro exemplo.txt
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/exemplo.txt'

#Abrir o ficheiro
try:
    #Abrir o ficheiro
    with open(caminho_ficheiro, 'r', encoding="utf-8") as ficheiro:
        #Ler e exibir o conteúdo do ficheiro linha por linha
        for linha in ficheiro:
            print(linha.strip()) # strip() remove espaços em branco e quebras de linha extras

except FileNotFoundError:
    print("O ficheiro não existe")
        
 