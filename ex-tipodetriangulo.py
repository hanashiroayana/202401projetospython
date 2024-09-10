a = float(input('Insira um valor: '))
b = float(input('Insira um valor: '))
c = float(input('Insira um valor: '))

if a+c>b and a+b>c and b+c>a:
    print('As retas podem formar um triâgulo!')
    if a != b and b != a and a != c:
        print('É um triângulo escaleno.')
    elif a == b == c:
        print('É um triângulo equilátero.')
    elif a == b or b == c or c == a:
        print ('É um triângulo isósceles')
else:
    print('As retas não podem formar um triângulo')