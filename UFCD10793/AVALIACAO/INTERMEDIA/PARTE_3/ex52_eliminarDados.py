import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

#Eliminar os funcionários com salário inferior a 3000
cursor.execute('DELETE FROM funcionarios WHERE salario < 3000')

conn.commit()
conn.close()

