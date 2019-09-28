from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento:'))
idade = atual-nascimento
print('Quem nasceu no ano de {} tem {} anos de Idade '.format(atual,idade))
if idade==18:
    print('Voce Precisa se Alistar!!')
elif idade>18:
    saldo=idade-18
    print('Voce Precisa Ir A Junta Urgentemente\n Voce Passou {} anos do seu alistamento'.format(saldo))
elif idade<18:
    saldo = 18-idade
    print('Ainda Faltam {} anos para Seu Alistamento'.format(saldo))