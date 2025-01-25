'''Faz um programa que receba três parâmetros inteiros (horas, minutos e segundos)
e converta o resultado para segundos'''

horas = int(input("Valor hora: "))
minutos = int(input("Valor minuto: "))
segundos = int(input("Valor segundo: "))

print(f"Hora convencional: {horas}:{minutos}:{segundos}")

total_seconds = horas * 3600 + minutos * 60 + segundos
print(f"Total de segundos: {total_seconds}")
