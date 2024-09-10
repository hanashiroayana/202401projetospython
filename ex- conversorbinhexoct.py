num = int(input('Digite um número: '))
base = int(input(f'Qual a sua base de conversão?\nDigite [1] para binário\nDigite [2] para octal\nDigite [3] para hexadecimal\n'))
bases=[1,2,3]
if base not in bases:
    print('Número inválido. Tente novamente.')
else:
    if base == 1:
        print('Número binário: {}'.format(bin(num)[2:]))
    elif base == 2:
        print('Número octal: {}'.format(oct(num)[2:]))
    else:
        print('Número hexadecimal: {}'.format(hex(num)[2:]))