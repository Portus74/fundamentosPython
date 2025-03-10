'''
Inserir dados na tabela
'''

import sqlite3
# Localização e ficheiro empresa.db
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_3/EXEMPLOS/universidade.db'

#Criar uma conexão a uma base de dados chamada universidade.db
conexao = sqlite3.connect(caminho_ficheiro)

#Criar um objeto cursos para interagir com a base de dados
cursor = conexao.cursor()


#Criar a tabela
cursor.execute('''
               CREATE TABLE IF NOT EXISTS alunos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   idade INTEGER NOT NULL,
                   curso TEXT NOT NULL
                   )
                   ''')

# Inserir alunos
cursor.execute("INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)", ('João', 21, 'Engenharia'))
cursor.execute("INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)", ('Maria', 22, 'Matemática'))
cursor.execute("INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)", ('Carlos', 23, 'Física'))

# Comitar as alterações
conexao.commit()
# Fechar a conexão
conexao.close()



print("Dados inseridos com sucesso!")
