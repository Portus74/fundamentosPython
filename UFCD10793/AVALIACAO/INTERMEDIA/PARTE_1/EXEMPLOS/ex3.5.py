#3v. Exemplo de KeyError: 
try: 
    dicionario = {"nome": "João"} 
    print(dicionario["idade"]) 
except KeyError: 
    print("Erro: Chave não encontrada no dicionário.") 
