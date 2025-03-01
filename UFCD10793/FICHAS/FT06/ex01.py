'''
Considera a lista:

cores = ["amarelo", "azul", "branco", "preto", "verde"]

Criar um programa em python que:

a. Faz o print de toda a lista
b. Faz o print do indíce 2 da lista
c. altera o índice 0 da lista para "vermelho"
d. Faz o print de toda a lista
e. Acrescenta no final da lista a cor "amarelo"
f. Faz o print de toda a lista
g. Acrescenta on indíce 2 a cor "roxooo"
h. Faz o print de toda a lista
i. Apaga o último elemento da lista
j. Faz o print de toda a lista
k. Faz o print do tamanho da lista (len)
'''

# Definir a lista inicial
cores = ["amarelo", "azul", "branco", "preto", "verde"]

# a. Faz o print de toda a lista
print("a. Lista completa:")
print(cores)

for cor in cores:
    print(cor)


# b. Faz o print do índice 2 da lista
print("\nb. Elemento no índice 2:")
print(cores[2])

# c. Altera o índice 0 da lista para "vermelho"
cores[0] = "vermelho"
print("\nc. Alterando o índice 0 para 'vermelho'")

# d. Faz o print de toda a lista
print("\nd. Lista após alteração:")
print(cores)

# e. Acrescenta no final da lista a cor "amarelo"
cores.append("amarelo")
print("\ne. Acrescentando 'amarelo' no final da lista")

# f. Faz o print de toda a lista
print("\nf. Lista após adicionar 'amarelo':")
print(cores)

# g. Acrescenta no índice 2 a cor "roxo"
cores.insert(2, "roxo")
print("\ng. Acrescentando 'roxo' no índice 2")

# h. Faz o print de toda a lista
print("\nh. Lista após adicionar 'roxo':")
print(cores)

# i. Apaga o último elemento da lista
cores.pop()
print("\ni. Removendo o último elemento da lista")

# j. Faz o print de toda a lista
print("\nj. Lista após remover o último elemento:")
print(cores)

# k. Faz o print do tamanho da lista (len)
print("\nk. Tamanho da lista:")
print(len(cores))