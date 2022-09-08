#Importando as classes:
from baralho import Baralho
from carta import Carta

#Instanciando uma carta fazendo uso dos métodos modificadores.
c = Carta('2', 'espada', 'vermelho')
#A versão do professor não permite essa modificação e quebra a execução do programa. A minha versão modifica e segue a execução.
c.valor = 'rei'
print(c)

def embaralhar():
    print('Função embaralhar()')

embaralhar()

#A geração das cartas está com os parâmetros naipe e valor com ordens invertidas.
baralho = Baralho(True)
baralho.embaralhar()

#Vai retirando e exibindo todas as cartas.
#for i in range(53):
    #print(baralho.retirarCarta())

#Faz o mesmo que o laço for acima.
while (baralho.temCarta()):
    carta = baralho.retirarCarta()
    print(carta)
print('Não há mais cartas a serem retiradas.')
print('Total de cartas no baralho: ', len(baralho))

#Devolve ao baralho duas cartas (quais?).
baralho.receberCarta(carta)
baralho.receberCarta(carta)
print('Total de cartas no baralho: ', len(baralho))
print(baralho)

#Instanciação de um novo baralho.
baralho2 = Baralho()
for i in range (42):
    baralho2.retirarCarta()
print('Baralho 2\n')
print(baralho2)

print('Fazer o baralho 1 receber as cartas do 2:')
baralho.juntarBaralho(baralho2)
print(baralho)
print(len(baralho))
print(len(baralho2))
input()

#Demostração de que atualmente o baralho recebe até elementos que não se enquadram em seu escopo.
alunos = {10: 'Lucas', 11: 'Luis', 12: 'Yago'}
baralho.container.append(alunos)
print(baralho)