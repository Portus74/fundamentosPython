import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

#Eliminar um funcionário
cursor.execute("DELETE FROM funcionarios WHERE nome = 'Mariana Costa'")

conn.commit()
conn.close()

