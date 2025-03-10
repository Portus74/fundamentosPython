'''
Considera o seguinte dicionário, a que cada prato é associado o respetivo 
valor em euros: 
'''
menu = {
    "entremeada": 7,
    "Sardinha": 6,
    "Filetes": 5.5,
    "Prego": 7,
    "Hamburguer": 5.5
}

#Efetua um programa em python que, após instanciar a variável: 

#a. Devolva o preço do “Prego”. 
print(f'Preço do prego = {menu["Prego"]} €')

#b. Faça o print de todas as chaves do dicionário
print(f'\nApresento todas as chaves do dicionário inicial\n{menu.keys()}')

#c. Acrescente na lista “Omolete” com o preço de 5.
menu["Omolete"] = 5

#d. Faça o print de todo o dicionário, para visualizar as alterações.
print(f'\nApresento todo o menu existente com o novo prato Omolete\n{menu}')
