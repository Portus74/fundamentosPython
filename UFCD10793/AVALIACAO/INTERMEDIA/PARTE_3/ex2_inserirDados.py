import sqlite3

conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

#Inserir funcionários na tabela
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Ana Silva', 'Gestora', 3500.0)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Pedro Santos', 'Programador', 2000.0)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Mariana Costa', 'Designer', 6000.0)")

cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Nelson Jesus', 'Suporte IT', 1750.0)")
cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Filipe Silva', 'Contabilista', 1500.0)")

# Guardar as mudanças e fechar a conexão
conn.commit()
conn.close()