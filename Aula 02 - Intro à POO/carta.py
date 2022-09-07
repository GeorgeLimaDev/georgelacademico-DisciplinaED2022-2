#Aula 2: Intro à POO. Exemplo: Criação de um baralho.
#Definindo a classe carta:

#A classe serve como um 'molde' para instanciar (gerar) objetos contendo todas as características (métodos) daquela classe.
class Carta:
    #Construtor: Método que atribui as principais propriedades da classe:
    def __init__(self, naipe, valor, cor):
        self.__naipe = naipe
        self.__valor = valor
        self.__cor = cor
    
    #Get é usado como convenção para métodos que retornam valores contidos em propriedades.
    def getValor(self):
        return self.__valor
    
    def getNaipe(self):
        return self.__naipe

    def getCor(self):
        return self.__cor
    
    #O método str serve para que o retorno contenha o dado. Sem ele o retorno exibe a posição de memória onde o dado foi alocado e não o dado em si.
    def __str__(self):
        return f'{self.__valor} de {self.__naipe}'