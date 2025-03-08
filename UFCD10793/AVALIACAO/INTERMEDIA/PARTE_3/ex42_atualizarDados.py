import sqlite3
# Localização e ficheiro empresa.db
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_3/empresa.db'

conn = sqlite3.connect(caminho_ficheiro)
cursor = conn.cursor()

#Atualizar o salário de todos os funcionários em 5%
cursor.execute("UPDATE funcionarios SET salario = salario * 1.05")

conn.commit()
conn.close()
