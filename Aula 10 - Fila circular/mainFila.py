from FilaSequencialCircular import *
#from FilaEncadeada import * (ainda não funcionou)

fila = Fila(10)

if fila.estaVazia():
    print('Fila está vazia')

if fila.estaCheia():
    print('Fila está cheia')

print('Tamanho: ', len(fila))

try:
    for i in range(10):
        fila.enfileira(f'Aluno{i+1} ')

    print(fila)

    print('Busca (aluno5): ', fila.busca('Aluno5 '))
    print('Elemento 10: ', fila.elemento(10))
    print()

    fila.esvazia()
    print(fila)
    print('Tamanho: ', len(fila))

except FilaException as fe:
    print(fe)