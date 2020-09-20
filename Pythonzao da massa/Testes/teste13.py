n = int(input('Escolha [1]->binario [2]->octal [3]->hexadecimal: '))
aux = [0, 0, 0, 0, 0, 0, 0, 0]
i = 0
if n == 1:
    number = int(input('Numero: '))
    while number/2 > 0:
        aux[i] = number % 2
        number = int(number/2)
        i = i + 1
    while i >= 0:
        print(aux[i], end='')
        i = i - 1
    print('')
elif n == 2:
    number = int(input('Numero: '))
    while number/8 > 0:
        aux[i] = number % 8
        number = int(number/8)
        i = i + 1
    while i >= 0:
        print(aux[i], end='')
        i = i - 1
    print('')
elif n == 3:
    number = int(input('Numero: '))
    while number/16 > 0:
        aux[i] = number % 16
        number = int(number/16)
        i = i + 1
    while i >= 0:
        print(aux[i], end='')
        i = i - 1
    print('')
