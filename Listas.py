Lista=[]
i=0
n=int(input('Digite o Tamanho da Lista \n'))
while i<n:
    Lista.append(int(input('Digite um valor para Posição {} '.format(i))))
    i+=1
x=int(input('Digite o valor para Buscar:\n'))
print("O Valor {} Aparece {}vez(es) na Lista".format(x,Lista.count(x)))
#Exercicio Da Lista de Vetores
#def Calculo(I,Lista,Y):
#    while I < len(Lista1):
#        if Lista1[I] % Y == 0:
#            Lista1.remove(Lista1[I])
#        I += 1
#    return Lista1
#Lista1 = [2,3,4,5,6,7,8,9,10,11]
#for I in range(2):
#    M = Calculo(1+I, Lista1, 2+I)
#print('A Lista Resultante é \n {}'.format(M))









