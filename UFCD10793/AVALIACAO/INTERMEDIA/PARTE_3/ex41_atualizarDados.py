import sqlite3
# Localização e ficheiro empresa.db
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_3/empresa.db'

conn = sqlite3.connect(caminho_ficheiro)
cursor = conn.cursor()

#Atualizar o salário de Pedro Santos
cursor.execute("UPDATE funcionarios SET salario = 5000 WHERE nome = 'Pedro Santos'")

conn.commit()
conn.close()
