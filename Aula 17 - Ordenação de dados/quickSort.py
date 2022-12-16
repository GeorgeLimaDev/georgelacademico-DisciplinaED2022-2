#Funcionamento: define um pivô (para facilitar no primeiro elemento  de cada conjunto), um marcador A, no elemento subsequente ao pivô, e um marcador B, no último elemento do array. O B vem percorrendo voltando até encontrar um valor menor que o A. Quando encontra troca o valor dos marcadores e segue voltando no array. Quando B chega na posição de A, a posição seguinte é a posição correta para o elemento marcado como pivô.

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