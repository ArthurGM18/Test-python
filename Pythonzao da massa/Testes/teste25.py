from random import randint
lista = list(range(5))
for i in range(5):
    lista[i] = randint(0, 10)
    print(lista[i], end=' ')
lista.sort()
print('\nmaior: {}'.format(lista[0]))
print('menor: {}'.format(lista[4]))
