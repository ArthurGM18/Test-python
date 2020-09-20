n0 = float(input('segmento: '))
n1 = float(input('segmento: '))
n2 = float(input('segmento: ')) 
if n0 + n1 < n2:
    print('não é um triangulo')
elif n0 + n2 < n1:
    print('não é um triangulo')
elif n1 + n2 < n0:
    print('não é um triangulo')
else:
    if n1 == n2 != n0 or n1 == n0 != n2 or n0 == n2 != n1:
        print('é um triangulo isoceles')
    elif n1 == n2 and n1 == n0:
        print('é um triangulo equilatero')
    else:
        print('é um triangulo escaleno')
