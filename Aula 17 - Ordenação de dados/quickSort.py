#Funcionamento: define um pivô (para facilitar, no primeiro elemento  de cada conjunto), um marcador A, no elemento subsequente ao pivô, e um marcador B, no último elemento do array. O B vem percorrendo voltando até encontrar um valor menor que o pivô, enquanto A percorre para a frente até encontrar alguém maior que o pivô. Quando ambos encontram, troca-se o valor dos marcadores e o processo de busca é retomado realizando trocas sempre que necessário. O processo de busca e troca é terminado quando B alcança um indice menor que o A. Nesse momento é determinada que a posição correta para o pivô é no marcador B, sendo realizada a troca entre eles. Na sequência o processo é reiniciado de forma recursiva nos subconjuntos a esquerda e direita do pivô original para determinar a posição correta de cada elemento de forma linear, fazendo com que cada elemento seja pivô durante as iterações.

def quickSort(array):
    quickSortRun(array, 0, len(array)-1)

def partition(array, low, high):
    pivot = array[low]
    a= low + 1
    b = high

    while True:
        while(a <= high and array[a] <= pivot):
            a += 1

        while (array[b] > pivot):
            b -= 1
        
        if (a < b):
            array[a], array[b] = array[b], array[a]
            a += 1
            b -= 1
        
        if (a > b):
            break

    array[low] = array[b]
    array[b] = pivot
    print(array) #Para acompanhar as trocas.

    return (b)

def quickSortRun (array, low, high):
    if (low < high):
        pi = partition(array, low, high)
        quickSortRun(array, low, pi-1)
        quickSortRun(array, pi+1, high)

print('Teste do Quick sort')
array = [20,5,15,4,2,9,11]
print('Array Original:',array)
quickSort(array)
print('Array Ordenado:',array)