'''
Escreve um programa que recebe o nome de um produto e o seu
preço, e retorne o preço total considerando os descontos seguintes:

1. Se o produto for um smartphone, será aplicado um desconto de 10%
2. Se o produto for um tablet, será aplicado um desconto de 15%
3. Se o produto for um laptop, será aplicado um desconto de 20%
4. Para qualquer outro produto, não haverá desconto

Utilize a estrutura match...case para determinar o desconto a ser aplicado
'''

'''Lista de produtos'''
produtos = {'smartphone': 0.10, 'tablet': 0.15, 'laptop': 0.20}

produto = input('Digite o nome do produto: ').lower()

# verifica se o preço é um número
while True:
    try:
        preco = float(input('Digite o preço do produto: '))
        break
    except ValueError:
        print('Preço inválido. Utilize apenas números')


match produto:
    case 'smartphone':
        preco_total = preco * (1 - produtos['smartphone'])
    case 'tablet':
        preco_total = preco * (1 - produtos['tablet'])
    case 'laptop':
        preco_total = preco * (1 - produtos['laptop'])
    case _:
        preco_total = preco

print(f'O preço total do produto é: {preco_total:.2f} €')


                    