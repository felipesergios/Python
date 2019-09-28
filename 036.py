casa  = float(input('Valor da Casa: R$'))
salário = float(input('Salário do Comprador'))
anos = int(input('Quantos Anos de financiamento'))
prestação = casa/(anos*12)
mínimo = salário * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa,anos))
print('a prestação será de R${:.2f}'.format(prestação))
if prestação<=mínimo:
    print('EMprestimo Aprovado')
else:
    print('Negado')