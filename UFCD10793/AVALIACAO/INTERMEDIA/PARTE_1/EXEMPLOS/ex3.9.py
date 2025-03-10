#3ix. Exemplo de IOError: 
try: 
    with open("dados.txt", "r") as f: 
        conteudo = f.read() 
except IOError: 
    print("Erro de entrada/saída ao abrir o ficheiro.") 
