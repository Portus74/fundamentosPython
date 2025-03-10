import copy

# a. Criar um dicionário inicial
computador1 = {
    "Marca": "Asus",
    "Ecra": "14Pol",
    "RAM": [4, 8, 12]
}
print("Computador 1:", computador1)

# b. Adicionar um novo elemento com chave "Disco"
computador1["Disco"] = ["128G", "256G"]
print("Computador 1 atualizado:", computador1)

# c. Permitir ao utilizador inserir um valor de RAM e verificar se existe
valor_ram = int(input("\nDigite um valor de RAM para verificar: "))
if valor_ram in computador1["RAM"]:
    print(f"O valor {valor_ram}GB está na lista de RAM.")
else:
    print(f"O valor {valor_ram}GB não está na lista de RAM.")

# d. Adicionar o valor 16 à RAM
computador1["RAM"].append(16)
print("\nComputador 1 com nova RAM:", computador1)

# e. Criar uma cópia profunda do dicionário
computador2 = copy.deepcopy(computador1)

# f. Modificar a cópia para ter "Lenovo" e RAM [4,8]
computador2["Marca"] = "Lenovo"
computador2["RAM"] = [4, 8]
print("Computador 2:", computador2)

# g. Criar outra cópia e modificar para "HP" e Disco ["256G"]
computador3 = copy.deepcopy(computador1)
computador3["Marca"] = "HP"
computador3["Disco"] = ["256G"]
print("Computador 3:", computador3)

# h. Criar uma lista com os três dicionários
lista_computadores = [computador1, computador2, computador3]

# i. Imprimir marcas que possuem disco de 128G
print("\nMarcas com 128G de Disco:")
for pc in lista_computadores:
    if "128G" in pc["Disco"]:
        print(pc["Marca"])

# j. Imprimir marcas com 8 e 12GB de RAM
print("\nMarcas com 8 e 12GB de RAM:")
for pc in lista_computadores:
    if 8 in pc["RAM"] and 12 in pc["RAM"]:
        print(pc["Marca"])
