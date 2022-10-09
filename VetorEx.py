
# Criando um vetor vazio
Lista=[]
# definindo o tamanho do vetor
n=int(input('Digite o Tamanho da Lista \n'))

#Funcao para iniciar o vetor de tamanho N
def initVector(n,Vetor):
    i=int(0)
    while i<n:
        Vetor.append(int(input("Informe o valor da posicao {} : \n".format(i))))
        i+=1
# Funcao para calcular o N**2 de cada posicao do vetor(atualizando o vetor já usado)
def powerUPVector(Vector):
    i=0
    while i<len(Vector):
        Vector[i]=Vector[i]**2
        i+=1
# Funcao para calcular o N**2 retornando um novo vetor
def powerUPCreatingNewVector(Vector):
    i=0
    while i<len(Vector):
        Vector[i]=Vector[i]**2
        i+=1
    return Vector


initVector(n,Lista) # Iniciando o vetor com o tamanho N
print(Lista) # Exibindo na tela os valores do vetor 
powerUPVector(Lista) # Calculando o N**2 e atualizando os valores no vetor atual
print(Lista) #Exibindo o valor atualizado do vetor na tela
# GERANDO NOVO VETOR 
print("Gerando um novo vetor com base no atual")
NovoVetor=powerUPCreatingNewVector(Lista) # Passando o vetor atual como parametro da funcao e jogando na var NovoVetor
print(NovoVetor)# Exibindo o novo vetor
