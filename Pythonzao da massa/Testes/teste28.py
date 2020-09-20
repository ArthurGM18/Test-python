lista = list()
pares = list()
impares = list()
for i in range(7):
    val = int(input('Valor: '))
    if val%2 == 0:
        pares.append(val)
    else:
        impares.append(val)
pares.sort()
impares.sort()
lista.append(pares)
lista.append(impares)
for i in range(2):
    print(lista[i])
