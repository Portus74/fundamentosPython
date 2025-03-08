import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

#Atualizar o salário de todos os funcionários em 5%
cursor.execute("UPDATE funcionarios SET salario = salario * 1.05")

conn.commit()
conn.close()
