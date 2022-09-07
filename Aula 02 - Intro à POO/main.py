#Importando a classe baralho, que já contém a classe carta.
from baralho import Baralho

#O baralho já tinha o método embaralhar. Porque foi criado outro aqui?
def embaralhar():
    print('Função embaralhar()')

embaralhar()

#Instanciação do objeto gerando o baralho:
baralho = Baralho()
baralho.embaralhar()

print()
#saída do baralho gerado já embaralhado:
print(baralho)
#Exibição da quantidade de cartas geradas:
print(len(baralho))