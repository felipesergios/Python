valor=int(input('Informe o Valor para conversão:'))
print("Escolha uma das bases para conversão:\n"
      "[1]converter em Binário\n"
      "[2]converter em Octal\n"
      "[3]converter em Hexadecimal")



escolha = int(input('Opção:'))
while(escolha!=0):
    if escolha == 1:
        print('O valor {} convertido em Binário é {}'.format(valor, bin(valor)[2:]))
        escolha = int(input('Opção:'))
    elif escolha == 2:
        print('O Valor {} Convertido em Octal é {}'.format(valor, oct(valor)[2:]))
        escolha = int(input('Opção:'))
    elif escolha == 3:
        print('O valor {} Convertido em Hexadecimal é {}'.format(valor, hex(valor)[2:]))
        escolha = int(input('Opção:'))
    else:
        print('Escolha invalida Tente Novamente')
print("Fim do Programa")


