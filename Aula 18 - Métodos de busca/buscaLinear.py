#Funcionamento: Percorre linearmente o conjunto comparando a chave ao valor armazenado na posição atual da iteração. É a busca mais simples de implementar porém é também a menos eficiente.

#Versão 1 (interativa):
def buscaLinear (array, chave):
    for i in range (len(array)):
        if (chave == array[i]):
            return i
    return -1

print('Teste da busca linear')
array = [20,5,15,4,2,9,11]
chave = 9
index = buscaLinear(array, chave)
if (index >= 0):
    print(f'Chave {chave} encontrada na posição {index+1} do array')


#Versão 2 (recursiva):
def buscaLinearRecursiva(array, index, chave):
    if (index >= len(array)):
        return -1 #caso base
    if (array[index] == chave):
        return index #se encontrar logo na primeira chamada
    else:
        return buscaLinearRecursiva(array, index + 1, chave)

print()
print('Teste da busca linear recursiva')
array = [20,5,15,4,2,9,11]
chave = 2
index = buscaLinearRecursiva(array, 0, chave)
if (index >= 0):
    print(f'chave {chave} encontrada na posição {index + 1}')


#Versão 3 (iterativa ordenada):
#OBS: Ordenar o array permite definir mais rápido se a chave não está contida no array, pois se ele estiver ordenado e o valor checado for maior que a chave, já se pode concluir que ela não está presente e a execução não precisa continuar.
def buscaLinearOrdenada (array, chave):
    for i in range (len(array)):
        if (chave == array[i]):
            return i
        elif (chave < array[i]):
            return -1
    return -1

print()
print('Teste da busca linear ordenada')
array = [20,5,15,4,2,9,11]
array = sorted(array)
chave = 4
index = buscaLinearOrdenada(array, chave)
if (index >= 0):
    print(array)
    print(f'Chave {chave} encontrada na posição {index+1} do array.')


#Versão 4 (recursiva ordenada):
def buscaLinearOrdenadaRecursiva (array, chave):
    return buscaLinearRecursiva(array, 0, chave) #usando a função criada anteriormente.

print()
print('Teste da busca linear recursiva ordenada')
array = [20,5,15,4,2,9,11]
array = sorted(array)
chave = 5
index = buscaLinearOrdenadaRecursiva(array, chave)
if (index >= 0):
    print(array)
    print(f'Chave {chave} encontrada na posição {index+1} do array.')
