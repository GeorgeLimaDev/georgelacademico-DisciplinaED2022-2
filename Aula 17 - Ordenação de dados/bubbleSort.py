#Funcionamento: Opera com "bolhas" que englobam dois elementos, o da iteração atual e seu vizinho seguinte. Compara os dois e efetua a troca caso o seguinte seja maior. Depois avança para o elemento seguinte e repete a operação até chegar ao fim do array.

#Versão 1:
def bolha (array):
    for i in range (len(array) - 1, 0, -1):
        for j in range (0, i):
            if (array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
        print(array) #Para acompanhar as trocas.

#Testes:
print('Teste do Bubble Sort')
array = [20,5,15,4,2,9,11]
bolha(array)

print()
print('*'* 50)
print()

#Versão 2:
def bolha2 (array):
    for i in range (len(array) - 1, 0, -1):
        troca = False
        for j in range (0, i):
            if (array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
                troca = True
        if (not troca):
            return
        print(array) #Para acompanhar as trocas.

#Testes:
print('Teste do Bubble Sort com flag')
array = [20,5,15,4,2,9,11]
bolha2(array)
print('Array ordenado: ', array)