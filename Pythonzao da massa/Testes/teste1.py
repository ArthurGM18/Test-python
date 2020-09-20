import random
n1 = str(input('nome: '))
n2 = str(input('nome: '))
n3 = str(input('nome: '))
n4 = str(input('nome: '))
list = [n1, n2, n3, n4]
random.shuffle(list)
print(list)
