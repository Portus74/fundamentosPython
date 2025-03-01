# Definir a lista inicial com diferentes tipos de dados
nums = [10, 2.5, 7, 11, 7.9, "Python", True, 6, 5.8, "Listas"]

# a. Imprima a quantidade de inteiros, floats, strings e booleanos na lista
contador_inteiros = 0
contador_floats = 0
contador_strings = 0
contador_booleanos = 0

for item in nums:
    if type(item) == int and item != True and item != False:  # Tratando inteiros puros (não booleanos)
        contador_inteiros += 1
    elif type(item) == float:
        contador_floats += 1
    elif type(item) == str:
        contador_strings += 1
    elif type(item) == bool:
        contador_booleanos += 1

print("a. Quantidade de cada tipo na lista:")
print(f"Inteiros: {contador_inteiros}")
print(f"Floats: {contador_floats}")
print(f"Strings: {contador_strings}")
print(f"Booleanos: {contador_booleanos}")

# b. Efetua a média de todos os valores inteiros na lista
soma_inteiros = 0
quantidade_inteiros = 0

for item in nums:
    if type(item) == int and item != True and item != False:  # Considerando apenas inteiros puros
        soma_inteiros += item
        quantidade_inteiros += 1

if quantidade_inteiros > 0:
    media_inteiros = soma_inteiros / quantidade_inteiros
    print("\nb. Média dos valores inteiros:")
    print(media_inteiros)
else:
    print("\nb. Não há valores inteiros na lista para calcular a média.")

# c. Crie e retorne uma nova lista só com os valores inteiros
inteiros = []

for item in nums:
    if type(item) == int and item != True and item != False:  # Considerando apenas inteiros puros
        inteiros.append(item)

print("\nc. Lista contendo apenas os valores inteiros:")
print(inteiros)