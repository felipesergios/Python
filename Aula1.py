nome = str(input('Qual seu nome:'))
if nome=='felipe':
    print('Que nome Bonito')
elif nome=='Paulo' or nome=='Maria' or nome=='Jose':
    print('Seu nome é bem popular')
elif nome in 'Ana Clara Maria Julia':
    print('Belo nome feminino')
else:
    print('seu nome é bem normal')
print('Tenha uma boa noite ,{} !'.format(nome))