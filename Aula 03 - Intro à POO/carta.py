#Aula 3: Introdução aos conceitos de métodos acessores e modificadores aplicados ao exemplo anterior do baralho.

class Carta:
    #Construtor: Método que atribui as principais propriedades da classe:
    def __init__(self, naipe, valor, cor):
        self.__naipe = naipe
        self.__valor = valor
        self.__cor = cor
    
    #Definição de um método acessor para a propriedade privada:
    @property
    def valor(self):
        return self.__valor
    
    #Definição do método modificador para a propriedade privada:
    @valor.setter
    def valor(self, novoValor):
        self.__valor = novoValor

    def getNaipe(self):
        return self.__naipe

    def getCor(self):
        return self.__cor
    
    def __str__(self):
        return f'{self.__valor} de {self.__naipe}'