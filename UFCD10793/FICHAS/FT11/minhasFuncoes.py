'''
1. Escreve uma função em Python que, dados a medida do comprimento dos trêslados de um triângulo diga se o mesmo é equilátero, isósceles ou escaleno.
'''
def tipo_triangulo(lado1, lado2, lado3):
    """Determina o tipo de triângulo baseado nos seus lados."""
    if lado1 == lado2 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isósceles"
    else:
        return "Escaleno"

'''
2. Escreve uma função em Python que, dados a medida do comprimento do lado deum quadrado imprima os valores do seu perímero e da sua área (area=lado x lado; perimetro = 4 x lado).
'''
def medidas_quadrado(lado):
    """Calcula perímetro e área de um quadrado."""
    perimetro = 4 * lado
    area = lado * lado
    return f"Perímetro: {perimetro}, Área: {area}"

'''
3. Escreve uma função em Python que dada uma lista de números imprime a somados valores dessa lista, o número de elementos da lista e a media desses valores.
'''
def estatisticas_lista(lista):
    """Calcula soma, quantidade e média dos elementos de uma lista."""
    soma = sum(lista)
    quantidade = len(lista)
    media = soma / quantidade if quantidade > 0 else 0
    return f"Soma: {soma}, Quantidade: {quantidade}, Média: {media:.2f}"

'''
4. Escreve uma função em Python que dada uma palavra retorne o número devogais nessa palavra.
'''
def conta_vogais(palavra):
    """Conta o número de vogais em uma palavra."""
    vogais = 'aeiouAEIOU'
    return sum(1 for letra in palavra if letra in vogais)

'''
5. Escreve uma função em Python que, dada uma lista de elementos, devolvaessa mesma lista, mas sem elementos repetidos.
'''
def remove_duplicados(lista):
    """Remove elementos duplicados de uma lista mantendo a ordem."""
    return list(dict.fromkeys(lista))

'''
6. Escreve uma função que, dado o número do mês retorne o mesmo, por extenso.
'''
def mes_por_extenso(numero):
    """Retorna o nome do mês correspondente ao número."""
    meses = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }
    return meses.get(numero, "Mês inválido")
