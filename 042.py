r1=float(input('R1:'))
r2=float(input('R2:'))
r3=float(input('R3:'))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Podem formar um Triangulo ',end='')
    if r1==r2==r3:
        print('Equilatero')
    elif r1!=r2!=r3!=r1:
        print('Escaleno')
    else:
        print('Isoceles')
else:
    print('Erro')
