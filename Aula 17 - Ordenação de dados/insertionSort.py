#Funcionamento: divide o array em dois conjuntos. O ordenado que começa recebendo o primeiro elemento do array, e o desordenado, recebendo o restante. O array desordenado é percorrido até encontrar o menor número, e quando ele é encontrado, é comparado com o valor do conjunto ordenado para saber em qual posição desse conjunto ele deve ser inserido, deslocando o restante dos elementos.

#Versão 1 (iterativa):
def insertionSort (array):
    for i in range (1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        
        array[j+1] = key
        print(array)

print('Teste do insertion Sort')
array = [20,5,15,4,2,9,11]
insertionSort(array)
print('Array ordenado: ', array)

#Versão 2 (recursiva):
from typing import List

def insertionSort2 (array):
    insertionSortRecursivo(array, len(array))

def insertionSortRecursivo (array:List[int], n:int):
    if n <= 1:
        return
    insertionSortRecursivo(array, n-1)

    ultimo = array[n-1]
    j = n-2

    while (j >= 0 and array[j] > ultimo):
        array[j+1] = array[j]
        j = j-1
    
    array[j+1] = ultimo
    print(array)

print()
print('Teste do insertion Sort recursivo')
array = [20,5,15,4,2,9,11]
insertionSort2(array)
print('Array Ordenado:',array)