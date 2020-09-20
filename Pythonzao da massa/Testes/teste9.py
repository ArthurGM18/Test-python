from random import randint
n = randint(0, 5)
n1 = int(input('Digite um numero de 0 a 5: '))
for i in range(2):
    print('voce tem {} tentativas'.format(3-i))
    n1 = int(input('Digite um numero de 0 a 5: '))
    if n1 == n:
        print('voce acertou')
        break
if n1 != n:
    print('voce perdeu')
