bl = True
lista = list(range(0))
while bl:
    num = int(input(''))
    if num in lista:
        print('Esse numero ja pertence a lista')
    else:
        lista.append(num)
    ch = str(input('Deseja continuar?[S/N] '))
    if ch == 'N' or ch == 'n':
        bl = False
lista.sort(reverse=True)
print('a lista possui {}'.format(len(lista)))
for i in range(len(lista)):
    print(lista[i], end=' ')
if 5 in lista:
    print('\n5 esta presente na lista')
else:
    print('\n5 nao esta presente')
