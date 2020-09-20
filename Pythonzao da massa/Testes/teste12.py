casa = int(input('Valor: '))
salario = int(input('Valor: '))
prestacao = int(input('Meses: '))
if casa/prestacao > salario*0.3:
    print('Compra negada!')
else:
    print('Compra confirmada!')
