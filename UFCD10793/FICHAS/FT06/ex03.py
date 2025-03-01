# Definir a lista inicial de idades
idades = [25, 15, 19, 22, 37, 78, 46, 2, 67]

# a. Indique quantas pessoas são menores de idade
menores_de_idade = 0
for idade in idades:
    if idade < 18:
        menores_de_idade += 1

print("a. Número de pessoas menores de idade:")
print(menores_de_idade)

# b. Ordene a lista por ordem decrescente
idades_ordenadas = sorted(idades, reverse=True)
print("\nb. Lista ordenada por ordem decrescente:")
print(idades_ordenadas)

# c. Pede ao utilizador uma idade e verifica se essa idade está na lista
idade_procurada = int(input("\nc. Digite uma idade para verificar se está na lista: "))

if idade_procurada in idades:
    print("A idade está na lista")
else:
    print("Não existe ninguém com essa idade na lista")