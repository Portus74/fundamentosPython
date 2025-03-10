#3iii. Exemplo de FileNotFoundError: 
try: 
    with open("arquivo_inexistente.txt", "r") as file: 
        conteudo = file.read() 
except FileNotFoundError: 
    print("Erro: O ficheiro não foi encontrado.") 