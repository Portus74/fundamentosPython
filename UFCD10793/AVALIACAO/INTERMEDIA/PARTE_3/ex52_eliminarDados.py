import sqlite3
# Localização e ficheiro empresa.db
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_3/empresa.db'

conn = sqlite3.connect(caminho_ficheiro)
cursor = conn.cursor()

#Eliminar os funcionários com salário inferior a 3000
cursor.execute('DELETE FROM funcionarios WHERE salario < 3000')

conn.commit()
conn.close()

