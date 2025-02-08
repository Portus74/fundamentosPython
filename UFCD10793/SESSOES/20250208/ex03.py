'''
Escreve um programa que calcula a soma dos 10
primeiros números inteiros positivos.
Devolve o resultado no ecrã
'''

soma = 0
i = 1
while i <= 10:
    soma = soma + i
    i = i + 1
else:
    print(f"Resultado : {soma}")