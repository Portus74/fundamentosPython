txt = "uFcd proRAMação eM pyTHON "

#Imprimir texto
print(txt)

#Imprimir Texto sem espaçamento inicial
txt = txt.strip()
print(txt)

#Imprimir frase até à palavra na 13ª posição
print(txt[:13])

#Imprimir últimos  caracteres da frase
print(txt[-5:])

#Imprimir frase em maiúsculas
txt = txt.upper()
print(txt)

#Formatação de strings
nome = "Sandra Oliveira"
print("O {} gosta muito da {}".format(nome, txt))

#aliena g)
print(f"O {nome} gosta muito da {txt}")

prov="""o pior cego é aquele que não quer ver."""

#Primeira letra da frase em maiúsculas
prov = prov.capitalize()
print(prov)
