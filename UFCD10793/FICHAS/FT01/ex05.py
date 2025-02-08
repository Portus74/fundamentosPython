'''Sejam a e b os catetos de um triângulo retângulo,
faz um programa que devolva o valor da hipotenusa'''

import math
cateto_a = int(input("Valor do cateto a: "))
cateto_b = int(input("Valor do cateto b: "))
hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
print("O valor da hipotenusa é: ", round(hipotenusa, 2))
