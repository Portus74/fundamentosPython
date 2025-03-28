from my_fancy_terminal import *

def quadrado(lado):
    area = lado * lado
    perimetro = 4 * lado
    output = f'Quadrado com lado {lado}'
    output += f'\n * Área: {area}'
    output += f'\n * Perímetro: {perimetro}'
    return output

# Testes
fprint(quadrado(1), cor=Cores.RED)  # Área: 1 Perímetro: 4
fprint(quadrado(2), cor=Cores.BLUE) # Área: 4 Perímetro: 8
fprint(quadrado(3), cor=Cores.RED)  # Área: 9 Perímetro: 12
fprint(quadrado(4), cor=Cores.BLUE) # Área: 16 Perímetro: 16