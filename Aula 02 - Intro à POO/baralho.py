#Importando a classe carta para fazer uso de deus métodos e propriedades na geração do baralho, no qual as cartas estão contidas.
from carta import Carta
import random

class Baralho:
    def __init__(self):
        #O container é iniciado como uma lista vazia que as cartas.
        self.container = list()
        naipe = ['ouro', 'espada', 'copa', 'paus']
        cor = ['vermelho', 'preto', 'vermelho', 'preto']
        valor = ['às', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'valete', 'dama', 'rei']

        #Esse laço popula o container com as cartas geradas de acordo com as iterações entre os elementos das variáveis naipe e valor. É aqui que as cartas são de fato geradas.
        for n in range(len(naipe)):
            for v in range(len(valor)):
                self.container.append(Carta(valor[v],naipe[n],cor[n]))
    
    #Método str para que o retorno exiba o conteúdo das cartas.
    def __str__(self):
        s = ''
        for carta in self.container:
            s += (carta.__str__() + '\n')
        return s
    
    #Geração de um método len próprio para essa classe. (Por qual motivo se faz necessário?)
    def __len__(self):
        return len(self.container)
    
    #Método embaralhar para colocar as cartas geradas em ordem aleatória.
    def embaralhar(self):
        random.shuffle(self.container)