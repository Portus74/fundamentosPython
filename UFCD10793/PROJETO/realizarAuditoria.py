import sqlite3
import psutil
import platform
from datetime import datetime

def coletar_informacoes():
    info = {
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "sistema": platform.system(),
        "versao": platform.version(),
        "cpu_uso": psutil.cpu_percent(interval=1),
        "memoria_disponivel": psutil.virtual_memory().available / (1024 *1024)
    }
    return info

def salvar_auditoria(dados):
    conexao = sqlite3.connect('auditoria.db')
    cursor = conexao.cursor()
    
    cursor.execute('''
                   INSERT INTO auditoria(data_hora, evento, detalhes) VALUES (?, ?, ?)''',
                   (dados["data_hora"], "Informações do Sistema", str(dados))
                   )
    conexao.commit()
    conexao.close()

# Exemplo de uso:
dados = coletar_informacoes()
salvar_auditoria(dados)