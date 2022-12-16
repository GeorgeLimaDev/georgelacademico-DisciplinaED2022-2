#Funcionamento: O array é dividido em dois de forma recursiva até que cada array contenha apenas um elemento. Neste momento os elementos são comparados e juntos novamente na ordem correta.

from typing import List

def mergeSort (array:List[int]):
    print(array)
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        mergeSort(right)
        mergeSort(left)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right [j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

print('Teste do Merge sort')
array = [25,48,37,12,57,83,33,92]
mergeSort(array)
print('Array Ordenado:',array)