#Importa a biblioteca sqlite3
#Esta biblioteca permite a interação com o banco de dados SQLite
import sqlite3

# Localização e ficheiro empresa.db
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_3/empresa.db'

#Estabelece a conexão com o banco de dados
conn = sqlite3.connect(caminho_ficheiro)

#Cria um cursor que será usado para executar comandos SQL
cursor = conn.cursor()

# Consultar os funcionários da tabela
cursor.execute("SELECT * FROM funcionarios")

# Obter os resultados da consulta, retorna todos os registos e armazena em funcionarios
funcionarios = cursor.fetchall()

#Percorre a lista de funcionarios e exibe os resultados
for funcionario in funcionarios:
    print(funcionario)

#Fecha a conexão
conn.close()
