'''
Criar uma tabela em sqlite3
'''

import sqlite3
# Localização e ficheiro empresa.db
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_3/EXEMPLOS/universidade.db'

#Criar uma conexão a uma base de dados chamada universidade.db
conexao = sqlite3.connect(caminho_ficheiro)

#Criar um objeto cursos para interagir com a base de dados
cursor = conexao.cursor()

#Criar uma tabela Alunos
cursor.execute('''
               CREATE TABLE Alunos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   idade INTEGER,
                   curso TEXT
                )
''')


print("Tabela 'Alunos' criada com sucesso")


#Fechar a conexão
conexao.commit()
conexao.close()

