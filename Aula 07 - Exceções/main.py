#Exercício: criar classes e tratar exceções para um projeto de banco.

from conta import Conta
from banco import *

try:
    bco = Banco()
    bco.addConta(123, 'Alex')
    bco.addConta(456, 'Clodoaldo')
    bco.addConta(457, 'George')
    bco.addConta(458, 'Márcio')
    bco.addConta(120, 'Caio')
    bco.addConta(121, 'Felipe')

    bco.sacar(456, 10.00)

except OperacaoInvalidaException as oie:
    print(oie)

print(bco)