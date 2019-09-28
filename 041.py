from datetime import date
Atual = date.today().year
Nascimento_do_Atleta=int(input('Digite Seu Nascimento Atleta:'))
Idade=Atual-Nascimento_do_Atleta
print('O Atleta tem {} Anos '.format(Idade))
if Idade<=9:
    print('MIRIM')
elif Idade<=14:
    print('INFANTIL')
elif Idade<=19:
    print('JUNIOR')
elif Idade<=25:
    print('Sênior')
elif Idade>25:
    print("MASTER")