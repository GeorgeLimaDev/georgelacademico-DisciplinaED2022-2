#Funcionamento: Pega o elemento da iteração e começa a percorrer os seguintes até encontrar o menor elemento seguinte. Ao encontrar, as posições deles são invertidos e a interação seguinte começa do próximo elemento do array uma vez que o menor já vai estar colocado na primeira posição.
#OBS: Só acontece uma troca por iteração, e sempre com o menor valor do array, ainda que ele não seja o menor imediato ao número da interação.

def selectionSort (array):
    for i in range (len(array) - 1):
        min = i
        for j in range (i + 1, len(array)):
            if (array[j] < array[min]):
                min = j
        array[min], array[i] = array[i], array[min]
        print(array) #Para acompanhar as trocas.


print('Teste do Selection sort')
array = [20,5,15,4,2,9,11]
selectionSort(array)
print()
print('Array ordenado: ', array)