tupla = ['Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.00, 'Canetas', 17.50, 'Livros', 18.00]
print('-------------------------------------')
print('       LISTA DE PREÇOS      ')
print('-------------------------------------')
for i in range(0, len(tupla)-1, 2):
    print(tupla[i], end='')
    print('.'*(28-len(tupla[i])), end='')
    print('R$ {}'.format(tupla[i+1]))
print('-------------------------------------')
