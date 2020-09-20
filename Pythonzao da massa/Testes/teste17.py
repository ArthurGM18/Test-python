for i in range(3, 30):
    aux = 0
    for j in range(2, i-1):
        if i%j == 0:
            aux = 1
            break
    if aux == 0:
        print(i)
