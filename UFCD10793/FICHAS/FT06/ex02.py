# Definir a lista inicial de notas
notas = [11.2, 15, 8.7, 17.2, 7.9]

# a. Acrescenta o valor 10.9 no final da lista e faz o print de toda a lista
notas.append(10.9)
print("a. Lista após adicionar 10.9:")
print(notas)

# b. Faz o print do tamanho da lista
print("\nb. Tamanho da lista:")
print(len(notas))

# c. Faz o print do valor mínimo da lista
print("\nc. Valor mínimo da lista:")
print(min(notas))

# d. Faz a média dos valores da lista
media = sum(notas) / len(notas)
print("\nd. Média dos valores da lista:")
print(media)
# Ou se quiser formatar para mostrar apenas 2 casas decimais:
print(f"Média formatada: {media:.2f}")