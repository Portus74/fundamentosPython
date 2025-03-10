#3viii. Exemplo de AttributeError: 
try: 
    numero = 5 
    numero.append(10) 
except AttributeError: 
    print("Erro: Objeto inteiro não tem atributo 'append'.") 