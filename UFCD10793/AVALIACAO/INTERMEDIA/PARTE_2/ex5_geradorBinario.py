

# Gerar um ficheiro binário de exemplo
def criar_ficheiro_binario(nome_ficheiro, tamanho_em_bytes):
    """Cria um ficheiro binário de exemplo com dados aleatórios."""
    import os
    with open(nome_ficheiro, "wb") as f:
        f.write(os.urandom(tamanho_em_bytes))  # Gera dados aleatórios

# Localização, ficheiro e tamanho
caminho_ficheiro = 'c:/FORMACAO/fundamentosPython/UFCD10793/AVALIACAO/INTERMEDIA/PARTE_2/exemplo.bin'
tamanho = 4096  # 4 KB

# Criar o ficheiro binário
criar_ficheiro_binario(caminho_ficheiro, tamanho)
print(f"Ficheiro binário '{caminho_ficheiro}' criado com {tamanho} bytes.")