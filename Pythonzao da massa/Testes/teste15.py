aux = [0, 0, 0, 0, 0, 0]
sum = 0
for i in range(0, 6):
    aux[i] = int(input('Numero: '))
    if aux[i]%2 == 0:
        sum += aux[i]
print(sum)
