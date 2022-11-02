class FilaException (Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Fila:
    def __init__(self, tamanho:int = 10):
        self.__frente = 0
        self.__final = -1
        self.__tamanho = tamanho
        self.__ocupados = 0
        self.__dados = [None for i in range (tamanho)]

    def estaVazia(self)-> bool:
        return self.__ocupados == 0
    
    def estaCheia(self)-> bool:
        return self.__ocupados == self.__tamanho
    
    def tamanho(self)->int:
        return self.__ocupados
    
    def __len__(self)->int:
        return self.__ocupados
    
    def elemento(self, posicao:int)-> any:
        try:
            assert posicao > 0 and posicao <= self.__ocupados
            inicio = self.__frente
            for i in range (posicao-1):
                inicio = (inicio + 1) % self.__tamanho
            
            return self.__dados[inicio]
        except AssertionError:
            raise FilaException(f'Posição inválida para a fila atual com {self.__tamanho} elementos.')
    
    def busca (self, conteudo:any)-> int:
        for i in range (len(self.__dados)):
            if self.__dados[i] == conteudo:
                return i+1
        raise FilaException (f'Valor {conteudo} não está na fila')

    def enfileira(self, conteudo:any):
        self.__dados.append(conteudo)
    
    def desenfileira(self)-> any:
        pass
    '''
        if self.estaVazia():
            raise FilaException (f'Fila vazia.')
        return self.__dados.pop()
    '''

    def __str__(self):
        s = ''
        for e in self.__dados:
            s+= f'{e}'
        return s

    def esvazia(self):
        pass