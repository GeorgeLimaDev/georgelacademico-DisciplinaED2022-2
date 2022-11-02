from FilaSequencialCircular import Fila

fila = Fila(10)

if fila.estaVazia():
    print('Fila está vazia')

if fila.estaCheia():
    print('Fila está cheia')

print('Tamanho: ', len(fila))

fila.enfileira('Olá, ')
fila.enfileira('mundo! ')
fila.enfileira('Meu ')
fila.enfileira('nome ')
fila.enfileira('é ')
fila.enfileira('George.')

print(fila) #Enfileirando atrás dos 10 elementos None. Seria interessante ir substituindo eles.

#print('Elemento 1: ', fila.elemento(1))