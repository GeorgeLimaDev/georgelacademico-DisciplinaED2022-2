#Definição da classe de captura de erros na data:
class DataInvalidaException(Exception):
    def __init__(self,msg):
        super().__init__(msg)


class Data:
    #Dicionário contendo os valores máximos permitidos para cada mês (não considera anos bissextos).
    __limite = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    #Neste método os dados inseridos já passam pelos respectivos métodos de validação.
    def __init__(self,dia:int,mes:int,ano:int):
        self.__mes = mes
        self.__validaMes(mes)        
        self.setDia(dia)
        self.__ano = ano
    
    def getDia(self) -> int:
        return self.__dia

    #Esse teste submete o dia para ser comparado com o valor máximo para o mês selecionado a partir do dicionário.
    def setDia(self, dia:int):
        if dia > self.__class__.__limite[self.__mes]:
            raise DataInvalidaException(f"O mês {self.__mes} só tem {self.__class__.__limite[self.__mes]} dias.")
        self.__dia = dia

    def __validaMes(self, mes:int):
        if mes < 1 or mes > 12:
            raise DataInvalidaException(f"Mês {mes} é inválido. Valor correto: 1 <= mes <= 12")

    @property
    def mes(self) -> int:
        return self.__mes
    @mes.setter
    def mes(self, mes:int):
        #Este teste é acionado caso o resultado seja false, o que indica que o mês digitado não está dentro do intervalo válido.
        if not self.__validaMes(mes):
            raise DataInvalidaException(f"Mês {mes} é inválido. Valor correto: 1 <= mes <= 12")
        self.__mes = mes
    
    @property
    def ano(self) -> int:
        return self.__ano
    
    #Não entendi esse assert.
    @ano.setter
    def ano(self, ano:int):
        try:
            assert ano > 0, f"{ano} é um ano inválido."
            self.__ano = ano
        except AssertionError as ae:
            raise DataInvalidaException(ae.__str__())

    #Por que esses números dois?
    def __str__(self)->str:
        # data_completa = str(self.__dia) + '/' + str(self.__mes) + '/' + str(self.__ano)
        return f'{self.__dia:02}/{self.__mes:02}/{self.ano}'


# programa de teste
#Técnica para execução do programa principal dentro do mesmo arquivo. Ao identar todo o programa dentro do teste, esse bloco de código é aplicado somente à função que corresponde ao programa principal (__main__).
if __name__ == '__main__':
    d1 = Data(28,2,2022)
    print(d1)
    d1.ano = 2023
    print(d1)
    try:
        print(d1.getDia())
        d1.setDia(5)
        d1.ano = 0
        d1.mes = 2
        print(d1)
        d1.dia = 30
        print(d1)
    except DataInvalidaException as die:
        print(die)

    d2 = Data(10,5,2022)
    print(d2)

    d3 = Data(7,9,2022)
    print(d3)

    print('Dados do objeto d1:\n', d1.__dict__)
    print('Dados do objeto d2:\n', d2.__dict__)
    print('Dados do objeto d3:\n', d3.__dict__)
    #print('Dados internos da classe:\n', Data.__dict__)
