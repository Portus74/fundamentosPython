'''Escreve um programa para classificar um triângulo de acordo com o comprimento dos seus lados. Considere as seguintes informações:
* Triângulo equilátero: todos os lados possuem o mesmo comprimento;
* Triângulo escaleno: todos os lados possuem comprimento diferente;
* Triângulo isósceles: caracterizado por ter dois lados com o mesmo comprimento'''

ladoA = int(input("Insira o lado A:"))
ladoB = int(input("Insira o lado B:"))
ladoC = int(input("Insira o lado C:"))
if ladoA == ladoB == ladoC:
    print("Triângulo equilátero")
elif ladoA != ladoB and ladoA != ladoC and ladoB != ladoC:
    print("Triângulo escaleno")
else:
    print("Triângulo isósceles")
    
