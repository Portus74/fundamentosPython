
import sqlite3

criarTabela = True
inserirDados = False
consultarDados = False

if criarTabela:
    #Criar conexão com o banco de dados (ou criar se não existir)
    conn = sqlite3.connect('empresa.db')
    #Criar cursor para executar comandos SQL
    cursor = conn.cursor()

    # Criar tabela de funcionários

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS funcionarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    cargo TEXT NOT NULL,
                    salario REAL NOT NULL
                    )
    ''')

    # Guardar as mudanças e fechar a conexão
    conn.commit()
    conn.close()


if inserirDados:
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()

    #Inserir funcionários na tabela
    cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Ana Silva', 'Gestora', 3500.0)")
    cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Pedro Santos', 'Programador', 2000.0)")
    cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES ('Mariana Costa', 'Designer', 6000.0)")

    # Guardar as mudanças e fechar a conexão
    conn.commit()
    conn.close()


if consultarDados:
    conn = sqlite3.connect('empresa.db')
    cursor = conn.cursor()
    # Consultar os funcionários da tabela
    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()

    # Exibir os resultados
    for funcionario in funcionarios:
        print(funcionario)

    conn.close()
