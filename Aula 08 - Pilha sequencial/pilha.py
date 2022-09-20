#Tratamento de exceção (deve ser criado antes da chamada na classe em que atua)
class pilhaException(Exception): #É acionada quando tenta-se acessar um índice não populado.
    def __init__(self, msg):
        super().__init__(msg) #msg é a string incluída na chamada da função.

#Definição da classe Pilha:
class pilha:
    def __init__(self):
        self.__dados = list()
    
    def estaVazia(self) -> bool:
        return len(self.__dados) == 0 #Retorna true se vazia ou false se populada.
    
    def tamanho(self) -> int:
        return len(self.__dados)
    
    def __len__(self) -> int:
        return len(self.__dados) #Definição de um método length próprio para esta classe.

    def elemento(self, posicao:int) -> any: #Busca um elemento da pilha a partir de uma posição e exibe seu conteúdo.
        try:
            return self.__dados[posicao-1]
        except IndexError:
            raise pilhaException(f'Posição inválida para a pilha atual com {len(self.__dados)} elementos.')
    
    def busca(self, conteudo:any) -> int: #Busca um elemento na pilha a partir de sua posição.
        for i in range(len(self.__dados)):
            if self.__dados[i] == conteudo:
                return i+1
        raise pilhaException(f'Valor {conteudo} não está na pilha.')
    
    def modificar(self, posicao: int, conteudo: any): #Altera um valor já definido na pilha.
        try:
            self.__dados[posicao-1] = conteudo
        except IndexError:
            raise pilhaException(f'Posição inválida par a pilha atual com {len(self.__dados)} elementos.')
    
    def empilha(self, conteudo:any):
        self.__dados.append(conteudo) #Append inclui um elemento na última posição da pilha

    def desempilha(self) -> any:
        if self.estaVazia():
            raise pilhaException(f'Pilha vazia.')
        return self.__dados.pop() #Pop retira o último elemento da pilha 
    
    def __str__(self): #Método para exibição do conteúdo da pilha.
        s = ''
        for i in self.__dados:
            s += f'{i}'
        return s
    
    def esvazia(self):
        self.__dados.clear() #Remove todos os elementos da pilha.