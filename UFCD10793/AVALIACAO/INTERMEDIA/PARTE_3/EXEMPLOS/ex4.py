'''
Ler dados da Base de dados
'''

import sqlite3
# Localização e ficheiro empresa.db
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_3/EXEMPLOS/universidade.db'

#Criar uma conexão a uma base de dados chamada universidade.db
conexao = sqlite3.connect(caminho_ficheiro)

#Criar um objeto cursos para interagir com a base de dados
cursor = conexao.cursor()

# Selecionar todos os alunos
sql = "SELECT * FROM alunos"
cursor.execute(sql)
# Obter os dados
alunos = cursor.fetchall()

#Exibir os alunos
for aluno in alunos:
    print(aluno)


# Comitar as alterações
conexao.commit()
# Fechar a conexão
conexao.close()



print("Dados inseridos com sucesso!")
