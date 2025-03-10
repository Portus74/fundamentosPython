dicionario = {
    "nome": "João",
    "idade": 25,
    "curso": "Informática"
}
print('Dicionário:', dicionario)

dicionario["morada"] = "     Rua das Flores      "
dicionario["telefone"] = 912345678
dicionario.pop("idade")

dicionario = {}
for chave, valor in dicionario.items():
    if isinstance(valor, str):
        dicionario[chave.upper()] = valor.strip()
    else:
        dicionario[chave.upper()] = valor

# EQUIVALENTE USANDO COMPREHENSION
dicionario = {chave.upper(): valor.strip() if isinstance(valor, str) else valor for chave, valor in dicionario.items()}

print('Dicionário:', dicionario)