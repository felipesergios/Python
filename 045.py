from random import randint
from time import sleep
itens =('Pedra','Papel','Tesoura')
computador=randint(0,2)
print('''SUAS OPÇÕES :
[0]--PEDRA
[1]--PAPEL
[2]--TESOURA''')
jogador=int(input('Sua Jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('-='*20)
print('o Computador escolheu {}'.format(itens[computador]))
print('O Jogador escolheu {}'.format(itens[jogador]))
print('-='*20)
if computador ==0:

    if jogador ==0:
        print('EMPATE')
    elif jogador==1:
        print('JOGADOR VENCE')
    elif jogador==2:
        print('COMPUTADOR VENCE')
    else:
        print('INVALIDA')


elif computador==1:
    if jogador ==0:
        print('COMPUTADOR VENCE')
    elif jogador==1:
        print('EMPATE')
    elif jogador==2:
        print('JOGADOR VENCE')
    else:
        print('INVALIDA')
    print('')
elif computador==2:
    if jogador ==0:
        print('JOGADOR VENCE')
    elif jogador==1:
        print('COMPUTADOR VENCE')
    elif jogador==2:
        print('EMPATE')
    else:
        print('INVALIDA')
    print('')
