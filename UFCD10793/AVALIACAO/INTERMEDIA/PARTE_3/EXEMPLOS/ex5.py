'''
Atualizar dados da Base de dados
'''

import sqlite3
# Localização e ficheiro empresa.db
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_3/EXEMPLOS/universidade.db'

#Criar uma conexão a uma base de dados chamada universidade.db
conexao = sqlite3.connect(caminho_ficheiro)

#Criar um objeto cursos para interagir com a base de dados
cursor = conexao.cursor()

# Atualizar a idade do aluno João
sql = "UPDATE alunos SET idade = 25 WHERE nome = 'João'"
cursor.execute(sql)

# Comitar as alterações
conexao.commit()
# Fechar a conexão
conexao.close()



print("Dados atualizados com sucesso!")
