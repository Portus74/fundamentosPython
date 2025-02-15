n =""
while not n.lstrip('-').isdigit():
    n = input('Numero: ')
    
n = int(n)



n = None
while n is None:
    try:
        n = int(input('Numero'))
    except:
        n = None

soma = 0
for i in range(1, n + 1):
    soma += i
print(soma)

