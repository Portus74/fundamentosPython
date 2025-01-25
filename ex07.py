'''Faz um programa que receba a distância em km e a quantidade em litros de
combustível consumido por um carro num percurso.
Calcula o consumo km/l e escreve uma mensagem de acordo com o resultado obtido.'''

distancia = int(input("Insira a distância percorrida: "))
litros = int(input("Insira a quantidade de combustível consumido: "))
consumo = round(distancia / litros, 2)

print(f"O consumo médio = {consumo} litros")

if consumo <= 5:
    print("O consumo é baixo")
elif consumo <= 8:
    print("O consumo é aceitável")
else:
    print("O consumo é alto")