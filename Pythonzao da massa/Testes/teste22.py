from random import randint
tupla = [0, 0, 0, 0, 0]
menor = 10
maior = 0
for i in range(5):
    tupla[i] = randint(0, 10)
    print(tupla[i], end=' ')
    if tupla[i] < menor:
        menor = tupla[i]
    if tupla[i] > maior:
        maior = tupla[i]
print('')
print(maior)
print(menor)
