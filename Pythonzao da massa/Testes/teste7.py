frase = str(input('Frase: '))
frase = frase.strip()
frase = frase.lower()
print(frase.count('a'))
for i in range(len(frase)):
    if frase[i] == 'a':
        print(i)
        break
i = len(frase)-1
while i > 0:
    if frase[i] == 'a':
        print(i)
        break
    i = i - 1
