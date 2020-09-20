peso = [0.0, 0.0, 0.0, 0.0, 0.0]
maior = 0.0
menor = 0.0
for i in range(5):
    peso[i] = float(input(''))
    if menor == 0.0:
        menor = peso[i]
    if peso[i] > maior:
        maior = peso[i]
    if peso[i] < menor:
        menor = peso[i]
print('o menor numero é:')
print(maior)
print('o maior numero é:')
print(menor)
