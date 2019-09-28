print('{:=^40}'.format(' Lojas Americanas '))
Preço=float(input('Preço das compras:'))
print('''   FORMAS DE PAGAMENTO 
[1]à vista dinheiro/cheque
[2]à vista no cartão
[3]2x no cartão
[4]3x ou mais no cartão''')
opção=int(input('Opção:'))
if opção==1:
    total = Preço-(Preço*10/100)
elif opção==2:
    total = Preço-(Preço*5/100)
elif opção==3:
    total=Preço
    parcela=total/2
    print('Sua compra foi parcelada em 2x de {:.2f}'.format(parcela))
elif opção==4:
    total=Preço+(Preço*20/100)
    total_de_parcela=int(input('Quantidade de Parcelas:'))
    parcela=total/total_de_parcela
    print('Sua Compra foi  dividida em {} parcelas de {:.2f}'.format(total_de_parcela,parcela))
print('Sua Compra de {:.2f} Vai Custar {:.2f}'.format(Preço,total))