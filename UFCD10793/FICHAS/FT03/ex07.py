'''Elabora um programa para verificar se um ano é bissexto ou não. A condição para ser ano bissexto é:
o ano deve ser divisível por 400
Ou se for divisível por 4 e não for divisível por 100'''

ano = int(input("Vamos determinar se ano é bissexto. Insira o ano pretendido:"))
if ano % 4 == 0 and (ano % 100 != 0 or ano %
                     400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
    
