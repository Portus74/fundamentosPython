'''
Faz um programa que escreva o nome do mês que é introduzido,
pelo utilizador, na forma numérica
'''
meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 
     4: 'Abril', 5: 'Maio', 6: 'Junho', 
     7: 'Julho', 8: 'Agosto', 9: 'Setembro',
     10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}

while True:
     numero_mes = int(input('Digite o número do mês: '))
     if 1 <= numero_mes <= 12:
          print(f'O mês {numero_mes} é {meses[numero_mes]}')
          break
     else:
          print("Mês desconhecido. Tenta novamente")

         