'''
Cria um menu interativo para gerir a base de dados onde o utilizador pode escolher entre:

1. Adicionar um novo funcionário
2. Listar todos os funcionários
3. Atualizar o salário de um funcionário
4. Eliminar um funcionário
5. Sair do programa
'''

import sqlite3

def adicionarFuncionario():
    nome = input("Nome: ")
    cargo = input("Cargo: ")
    salario = float(input("Salário: "))
    cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)", (nome, cargo, salario))
    
def listarFuncionarios():
    cursor.execute("SELECT * FROM funcionarios")
    for funcionario in cursor.fetchall():
        print(funcionario)
        
def atualizarSalario():
    nome = input("Nome do funcionário: ")
    novo_salario = float(input("Novo salário: "))
    cursor.execute("UPDATE funcionarios SET salario = ? WHERE nome = ?", (novo_salario, nome))

def eliminarFuncionario():
    nome = input("Nome do funcionário: ")
    cursor.execute("DELETE FROM funcionarios WHERE nome = ?", (nome,))
    

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar um novo funcionário")
        print("2. Listar todos os funcionários")
        print("3. Atualizar o salário de um funcionário")
        print("4. Eliminar um funcionário")
        print("5. Sair do programa")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionarFuncionario()
        elif opcao == "2":
            listarFuncionarios()
        elif opcao == "3":
            atualizarSalario()
        elif opcao == "4":
            eliminarFuncionario()
        elif opcao == "5":
            conn.commit()
            conn.close()
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


#Criar conexão
conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

menu()