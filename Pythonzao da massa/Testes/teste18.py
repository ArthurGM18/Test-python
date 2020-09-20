frase = str(input())
frase = frase.re
j = len(frase) - 1
aux = 0
for i in range(int(len(frase)/2)):
    if frase[i] != frase[j]:
        print('Nao é palindromo!')
        aux = 1
        break
    j -= 1
if aux == 0:
    print('é um palindromo!')

