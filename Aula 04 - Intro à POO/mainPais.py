#Importando a classe criada:
from Pais import Pais

#Instanciando dois objetos a partir da classe Pais:
pais1 = Pais('Brasil', 'Brasília', 4000)
pais2 = Pais('Argentina', 'Buenos Aires', 2000)

#Teste da saída dos objetos exibindo todos os atributos:
print(pais1)
print(pais2)

#Adição de países vizinhos ao Brasil:
pais1.addPaisDeFronteira('Uruguai')
pais1.addPaisDeFronteira('Argentina')
pais1.addPaisDeFronteira('Paraguai')
pais1.addPaisDeFronteira('Peru')
#Teste da resistência a itens duplicados (esta entrada não deve ser aceita pois é duplicada):
pais1.addPaisDeFronteira('Peru')

#Saída
print(f'Países vizinhos de {pais1.nome} : {pais1.vizinhos}')