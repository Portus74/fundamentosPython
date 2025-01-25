#imprimir o meu nome no ecran
print("Nelson Jesus")
print("Estou a frequentar formação de PYTHON pela EISNT")

num = input("Digite o ano nascimento: ")
print("Nasceu no ano", num)

print("Ano nascimento =", num,",\no quadrado do ano nascimento = ", int(num) ** 2)

#formatação posicional %d para inteiro, %s string, %f para decimal
print("Ano nascimento = %d,\no quadrado do ano nascimento = %f"%(int(num), round(int(num) ** 2, 0)))

#usando o format
print("Ano nascimento ={},\no quadrado do ano nascimento = {}".format(num, int(num) ** 2))

#mais atual e mais eficiente
print(f"Ano nascimento ={num}\no quadrado do ano nascimento = {int(num) ** 2}")
