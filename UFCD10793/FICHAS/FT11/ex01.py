'''
Podemos usar este código de forma a importar uma função específica
from minhasFuncoes import tipo_triangulo
e desta forma não tenho de definir o nome do módulo dentro da função print

Ou em alternativa posso usar
import minhasFuncoes

desta forma tenho de definir o nome do módulo dentro da função print
'''

import minhasFuncoes as myF
# Exemplos de uso das funções
def main():
    # Teste 1: Tipo de triângulo
    print("\n=== Teste do Triângulo ===")
    print(myF.tipo_triangulo(5, 5, 5))  # Equilátero
    print(myF.tipo_triangulo(5, 5, 3))  # Isósceles
    print(myF.tipo_triangulo(3, 4, 5))  # Escaleno


if __name__ == "__main__":
    main()