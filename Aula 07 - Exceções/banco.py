from conta import Conta
from typing import List

#Classe que recebe os tratamentos de exceções:
class OperacaoInvalidaException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class Banco:
    def __init__(self):
        self.__contas = dict()
        self.__saldoTotal = 0 #Soma do total de todos os clientes.

    def sacar(self, numero:int, quantia:float):
        try:
            assert quantia > 0 #Valor do saque deve ser positivo.
            # obter o objeto correspondente à conta
            conta = self.__contas[numero]
            #Só autoriza o saque caso ela não zere ou negativa o saldo.
            if conta.saldo - quantia >= 0:
                conta.saldo -= quantia
            else:
                raise OperacaoInvalidaException(f' Conta {numero}: Saldo insuficiente para saque')
        #Exceções de valor negativo e número de conta inválida.
        except AssertionError:
            raise OperacaoInvalidaException('Quantia a retirar não pode ser negativa')
        except KeyError:
            raise OperacaoInvalidaException(f'Conta {numero} não está cadastrada')

    #A implementar depois.
    def depositar(self, numero:int, quantia:float):
        pass
    
    #Verifica se o número da nova conta já existe. Se der false a nova conta é adicionada.
    def addConta(self, numero:int, titular:str):
        if numero not in self.__contas.keys():
            self.__contas[numero] = Conta(numero,titular)
        else:
            raise OperacaoInvalidaException(f'Conta de numero {numero} já está cadastrada')

    #Método str para exibição de todas as contas e seus respectivos dados.
    def __str__(self):
        s = ''
        cont = 1
        for key in self.__contas.keys():
            s+= f'{cont:02}: {key}, titular {self.__contas[key].titular}, saldo =  {self.__contas[key].saldo}\n'
            cont += 1
        return s

