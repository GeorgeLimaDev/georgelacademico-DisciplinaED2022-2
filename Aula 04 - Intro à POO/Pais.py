#Aula 04: Prática de exercícios em POO respondendo a seguinte questão:
'''
Escreva uma classe que represente um país. Um país tem como atributos privados o seu nome,
o nome da capital, sua dimensão em Km2 e uma lista de países com os quais ele faz fronteira. Represente a classe e forneça os seguintes construtores e método:
a) Construtor que inicialize o nome, capital e a dimensão do país;
b) Métodos de acesso para os atributos indicados no item (a);
c) Método que retorne a lista de países que fazem fronteira;
d) Método que adiciona o nome de país, a lista de fronteiras(verificar se o nome já existe na lista).
e) Método __str__(self).
'
'''

#Pra que serve esse import?
from typing import List

#Resposta ao item A do exercício (método construtor):
class Pais:
    def __init__(self, nome:str, capital:str, dimensao:int):
        self.__nome = nome
        self.__capital = capital
        self.__dimensao = dimensao
        self.__vizinhos = list()
    
    #Respostas ao item B do exercício (métodos de acesso):
    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def capital(self) -> str:
        return self.__capital
    
    @property
    def dimensao(self) -> int:
        return self.__dimensao
    
    #Resposta ao item C do exercício (retorna a lista de fronteiriços):
    @property
    def vizinhos(self) -> List[str]:
        return self.__vizinhos
    
    #Resposta ao item D do exercício (Adiciona um país ao fim da lista de fronteiriços):
    def addPaisDeFronteira(self, nome_do_pais:str):
        #O teste abaixo faz com que somente valores distintos sejam adicionados à lista.
        if nome_do_pais not in self.__vizinhos:
            self.__vizinhos.append(nome_do_pais)

    #Resposta ao item E do exercício (método de retorno dos dados adicionados ao objeto):
    def __str__(self):
        return f'{self.__nome}, Capital: {self.__capital}, Dimensão: {self.__dimensao} Km²'