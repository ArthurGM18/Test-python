lista = list()
dados = ['Nome', 0.0]
bl = True
i = 0
aux = ['Nome', 0.0]
while bl:
    dados[i] = str(input('Nome: '))
    dados[i+1] = float(input('Peso: '))
    lista.append(dados)
    ch = str(input('Deseja inserir mais dados?[S/N] '))
    if ch == 'n' or ch == 'N':
        bl = False
print('Tamanho da lista: {}'.format(len(lista)))
print('Lista das mais pesadas:')
for i in range(len(lista)):
    for j in range(len(lista)):
        if lista[j][1] > lista[i][1]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
for i in range(len(lista)):
    print('Nome: {} - Peso: {}'.format(lista[i][0], lista[i][1]))
