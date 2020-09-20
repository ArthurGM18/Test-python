matriz = [[0, 0, 0], [0, 0, 0,], [0, 0, 0]]
sum = 0
sum1 = 0
maior = -1000
for i in range(3):
    for j in range(3):
        val = int(input(''))
        sum += val
        if j == 2:
            sum1 += val
        if i == 1 and val > maior:
            maior = val
        matriz[i][j] = val
print(matriz)
print('soma: {}'.format(sum))
print('soma coluna 3: {}'.format(sum1))
print('maior da 2 coluna: {}'.format(maior))
