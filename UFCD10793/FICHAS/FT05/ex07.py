'''
Crie um programa para controlar listas, com as seguintes funções:

* Adicionar elemento no início
* Adicionar elemento no fim
* Remover elemento
* Tamanho da lista
* Imprimir elementos da lista
* Esvaziar lista
'''
lista = []

lista.insert(0, 10)
print(f"{10} adicionado no início.")

lista.append(20)
print(f"{20} adicionado no fim.")

lista.append(30)
print(f"{30} adicionado no fim.")

print("Elementos da lista:", lista)

if 20 in lista:
    lista.remove(20)
    print(f"{20} removido.")
else:
    print(f"{20} não encontrado na lista.")

print(f"Tamanho da lista: {len(lista)}")

print("Elementos da lista:", lista)

lista.clear()
print("Lista esvaziada.")

print("Elementos da lista:", lista)

