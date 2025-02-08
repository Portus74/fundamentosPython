'''
Elabora um programa para calcular a soma dos N primeiros
números naturais {1+2+3+...+N} em que N é um número introduzido
pelo utilizador
(NOTA: este programa poderia ser feito utilizando a formula da
progressão aritmética, S = (1+N) * N/2
mas faz de conta que não sabíamos a fórmula)
'''

while True:
    try:
        n = abs(int(input("Introduza um número: ")))
        break
    except ValueError:
        print("Erro: Por favor, introduza um número inteiro.")
        
i = 1
soma = 0
while i <= n:
    soma += i
    i += 1

print("A soma dos primeiros", n, "números naturais é:", soma)

            