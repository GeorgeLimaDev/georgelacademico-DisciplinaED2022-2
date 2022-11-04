class PilhaException(Exception):
    def __init__(self, msg):
        super().__init(msg)

#A pilha encadeada usa nós para ligar os elementos, dessa forma eles podem ocupar espaços de memória dinamicamente, desde que um aponte para o outro.
#Cada nó contém a carga (dado) a ser armazenada e um apontador para o próximo nó.
class knot:
    def __init__(self, carga:any):
        self.carga = carga
        self.prox = None #Apontar para None significa o fim da pilha.
    
    def __str__(self):
        return str(self.carga)

class Pilha:
    def __init__(self):
        self.__start = None #Muda dinamicamente conforme elementos são empilhados.
        self.__tamanho = 0

    def estaVazia(self) -> bool:
        return self.__start == None

    def tamanho(self) ->int:
        #Revisar o motivo desta parte estar comentada:
        '''
        cont = 0
        cursor = self.__head
        while (cursor != None):
            cont += 1
            cursor = cursor.prox
        return cont
        '''
        return self.__tamanho

    def __len__(self) ->int:
        return self.__tamanho

    #Falta implementar o próximo apontador e a carga.
    def elemento(self, posicao:int) ->any:
        try:
            #O deslocamento deve ser feito com uma variável a parte para que não se perca os apontadores armazenados nas variáveis já existentes.
            assert posicao > 0 and posicao <= self.__tamanho
            deslocamento = self.__tamanho - posicao
            cont = 0
            cursor = self.__start
            while (deslocamento > cont):
                cont += 1
                cursor = cursor.prox
            return cursor.carga
        except AssertionError:
            raise PilhaException(f'Posição inválida para a pilha atual com {len(self.__dados)} elementos.')

    #Retorna a posição do elemento buscado.
    def busca(self, conteudo:any) ->int:
        cursor = self.__start
        cont = 0
        while (cursor != None):
            if cursor.carga == conteudo:
                return self.__tamanho - cont
            cont += 1
            cursor = cursor.prox
        raise PilhaException(f'Valor {conteudo} não está na pilha.')

    def modificar(self, posicao:int, conteudo:any):
        try:
            self.__dados[posicao-1] = conteudo
        except IndexError:
            raise PilhaException(f'Posição inválida para a pilha atual com {len(self.__dados)} elementos.')

    def empilha(self, conteudo:any):
        self.__dados.append(conteudo)

    def desempilha(self) ->any:
        if self.estaVazia():
            raise PilhaException('Pilha vazia.')
        return self.__dados.pop()

    def __str__(self):
        s = ''
        for e in self.__dados:
            s += f'{e}'
        return s
    
    def esvazia(self):
        self.__dados.clear()