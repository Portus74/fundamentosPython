#Efetua um programa em python onde:

# a.Cries um dicionário e efetues o respetivo print
meu_dicionario = {
    "nome": "João",
    "idade": 25,
    "cidade": "Lisboa"
}
print("\nDicionário inicial:\n", meu_dicionario)

# b. Acrescentes dois novos elementos ao dicionário
meu_dicionario["profissao"] = "Engenheiro"
meu_dicionario["pais"] = "Portugal"
print("\nDicionário após adicionar elementos:\n", meu_dicionario)

# c. Removes um dos elementos da lista
del meu_dicionario["idade"]
print("\nDicionário após remoção:\n", meu_dicionario)

# d. Efetues uma operação, à escolha, sobre os dados no dicionário
tamanho = len(meu_dicionario)
print("\nNúmero de elementos no dicionário: ", tamanho)
