# String com as datas
datas = "12ago2021,02set2020,20jan2022,11out2019,09mar2020,10dez2022"

# a. Armazenar as datas numa lista usando split
lista_datas = datas.split(',')
print("Lista de todas as datas:")
print(lista_datas)
print()

# b. Imprimir datas de 2022 usando list comprehension
datas_2022 = [data for data in lista_datas if data[-4:] == "2022"]
print("Datas do ano 2022:")
print(*datas_2022, sep='\n')  # usando * para desempacotar a lista
print()

# c. Criar lista com os dias e ordenar usando list comprehension
dias = sorted([int(data[:2]) for data in lista_datas])
print("Lista de dias ordenada:")
print(dias)

# Bônus: podemos fazer outras operações interessantes com list comprehensions
# Extrair todos os meses
meses = [data[2:5] for data in lista_datas]
print("\nLista de meses:")
print(meses)

# Extrair todos os anos
anos = sorted(set(int(data[-4:]) for data in lista_datas))
print("\nAnos únicos em ordem crescente:")
print(anos)