#Importando a classe carta para fazer uso de deus métodos e propriedades na geração do baralho, no qual as cartas estão contidas.
from carta import Carta
import random

class Baralho:
    def __init__(self, embaralhar:bool = False):
        #O container é iniciado como uma lista vazia que as cartas.
        self.container = list()
        valor = ['às', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'valete', 'dama', 'rei']
        naipe = ['ouro', 'espada', 'copa', 'paus']
        cor = ['vermelho', 'preto', 'vermelho', 'preto']

        for n in range(len(naipe)):
            for v in range(len(valor)):
                self.container.append(Carta(valor[v],naipe[n],cor[n]))
        
        if embaralhar:
            self.embaralhar()
    
    def __str__(self):
        s = ''
        for carta in self.container:
            s += (carta.__str__() + '\n')
        return s
    
    def __len__(self):
        return len(self.container)
    
    #Adição do método embaralhar, anteriormente presente no programa principal.
    def embaralhar(self):
        random.shuffle(self.container)

    #A função pop retira de uma lista o último elemento.
    def retirarCarta(self) -> Carta:
        return self.container.pop()
    
    #Método para checar se ainda existem cartas no baralho para serem retiradas:
    def temCarta(self) -> bool:
        if len(self.container) == 0:
            return False
        else:
            return True
    
    #Método que retorna ao baralho uma carta retirada.
    def receberCarta(self, carta:Carta) -> bool:
        if carta not in self.container:
            self.container.append(carta)
            return True
        return False

    #Não ficou claro o que esse método faz:
    def juntarBaralho(self, outroBaralho):
        for i in range (len(outroBaralho)):
            carta_retirada = outroBaralho.retirarCarta()
            if not self.receberCarta(carta_retirada):
                outroBaralho.receberCarta(carta_retirada)