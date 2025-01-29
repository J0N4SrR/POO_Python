# Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

num = int(input('Digite um numero inteiro:\n'))
resto = num % 2
if resto == 0:
    print('O numero é par!')
else:
    print('O numero é impar!')