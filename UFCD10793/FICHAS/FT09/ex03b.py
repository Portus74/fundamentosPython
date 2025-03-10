import copy

# a. Instanciar o dicionário
Computadores_1 = {
    "Marca": "Asus",
    "Ecra": "14Pol",
    "RAM": [4, 8, 12]
}

# b. Acrescentar um novo elemento
Computadores_1["Disco"] = ["128G", "256G"]

# c. Verificar se um valor de RAM está na lista
valor_ram = int(input("Introduza um valor de RAM para verificar: "))
if valor_ram in Computadores_1["RAM"]:
    print(f"O valor {valor_ram}GB está presente na lista de RAM.")
else:
    print(f"O valor {valor_ram}GB não está presente na lista de RAM.")

# d. Acrescentar 16 como novo valor de RAM
Computadores_1["RAM"].append(16)

# e. Copiar o dicionário usando Deep Copy
Computadores_2 = copy.deepcopy(Computadores_1)

# f. Modificar a marca para "Lenovo" e os valores de RAM para [4,8]
Computadores_2["Marca"] = "Lenovo"
Computadores_2["RAM"] = [4, 8]
print("Computador 2:", Computadores_2)

# g. Criar nova cópia e modificar a marca para "HP" e Disco para ["256G"]
Computadores_3 = copy.deepcopy(Computadores_1)
Computadores_3["Marca"] = "HP"
Computadores_3["Disco"] = ["256G"]
print("Computador 3:", Computadores_3)

# h. Criar uma lista com os três dicionários
lista_computadores = [Computadores_1, Computadores_2, Computadores_3]

# i. Imprimir marcas com 128G de RAM
print("Marcas com 128G de Disco:")
for computador in lista_computadores:
    if "128G" in computador["Disco"]:
        print(computador["Marca"])

# j. Imprimir marcas com 8 e 12 de RAM
print("Marcas com 8 e 12 de RAM:")
for computador in lista_computadores:
    if 8 in computador["RAM"] and 12 in computador["RAM"]:
        print(computador["Marca"])
