Peso=float(input('Digite seu Peso:'))
Altura=float(input('Digite Sua Altura:'))
imc = Peso/(Altura**2)
print('O IMC Vale {:.1f}'.format(imc))
if imc<18.5:
    print('Abaixo do Peso')
elif 18.5<=imc<25:
    print('Peso Ideal')
elif 25<=imc<30:
    print('SobrePeso')
elif 30<=imc<40:
    print('Obesidade')
elif imc>=40:
    print('Morte')
