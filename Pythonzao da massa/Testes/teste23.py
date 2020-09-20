tupla = [0, 0, 0, 0, 0]
aux = 0
for i in range(5):
    tupla[i] = str(input(''))
    if '9' in tupla[i]:
        aux += tupla[i].count('9')
    if '3' in tupla[i]:
        print('posição: {}'.format(i))
    if int(tupla[i])%2 == 0:
        print('{} é par!'.format(tupla[i]))
print('noves: {}'.format(aux))
