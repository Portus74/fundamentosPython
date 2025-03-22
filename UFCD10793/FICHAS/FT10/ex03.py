
# String com as datas
datas = "12ago2021,02set2020,20jan2022,11out2019,09mar2020,10dez2022"

# a. Armazenar as datas numa lista
lista_datas = datas.split(',')
print("Lista de todas as datas:")
print(lista_datas)
print()

# b. Imprimir datas de 2022
print("Datas do ano 2022:")
for data in lista_datas:
    if data[-4:] == "2022":  # verifica os últimos 4 caracteres (ano)
        print(data)
print()

# c. Criar lista com os dias e ordenar
dias = []
for data in lista_datas:
    dias.append(int(data[:2]))  # pega os 2 primeiros caracteres (dia)

dias.sort()  # ordena a lista em ordem crescente
print("Lista de dias ordenada:")
print(dias)