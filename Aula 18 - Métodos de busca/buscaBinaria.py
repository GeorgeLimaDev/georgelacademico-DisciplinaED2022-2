#Funcionamento: Começa checando o elemento no centro do array ordenado e o compara a chave. Se for maior a busca precisa continuar somente no subconjunto a esquerda, e se for menor, a busca continua somente no subconjunto da direita. Reduz substancialmente o tempo de execução pois a cada iteração o array a ser checado diminui o tamanho pela metade.

def buscaBinaria (array, chave):
    inicio = 0
    fim = len(array) - 1
    while (inicio <= fim):
        meio = (inicio + fim) // 2
        if (chave < array[meio]):
            fim = meio - 1 #Leva a busca para o subconjunto a esquerda da chave
        elif (chave > array[meio]):
            inicio = meio + 1 #Leva a busca para o subconjunto a direita da chave.
        else:
            return meio
    return -1


print('Teste da busca binária')
array = [20,5,15,4,2,9,11]
array = sorted(array)
chave = 9
index = buscaBinaria(array, chave)
if (index >= 0):
    print(array)
    print(f'Chave {chave} encontrada na posição {index+1} do array.')
