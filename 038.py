num1=int(input('Primeiro numero :'))
num2=int(input('Segundo numero:'))
if num1==num2:
    print('os numeros são iguais')
elif num1>num2:
    print('O {} é maior que {}'.format(num1,num2))
elif num2>num1:
    print('O {} é maior que {}'.format(num2,num1))
