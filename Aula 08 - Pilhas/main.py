from pilha import *

numeros = [10,9,8,7,6,5,4,3,2]

pilha = pilha() #Estanciando um objeto a partir da classe pilha
for i in numeros:
    pilha.empilha(i) #Populando a pilha a partir de um laço.

print('Array: ', numeros)
print('Pilha: ', pilha)
pilha.empilha(1)
print('Pilha: ', pilha)
pilha.desempilha()
print('Pilha: ', pilha)
pilha.esvazia()

#Utilizando a estrutura de pilha para inverter uma lista:
string = 'George Lima'
print(string)
for i in string:
    pilha.empilha(i)
print()

while (not pilha.estaVazia()): #Enquanto a pilha não estiver vazia o laço repete exibindo o último elemento desempilhado.
    print(pilha.desempilha(),end='')
print()

#Testando o tratamento de exceção:
try:
    print(pilha.busca(5)) #Neste momento a pilha está vazia, então o resultado da busca causaria um erro capturado abaixo.
except pilhaException as pe:
    print(pe)

#Dúvidas:
#1: Qual a distinção entre os métodos elemento e busca?
#2: O tratamento de exceção para a busca poderia ficar dentro do método, deixando no programa principal somente a chamada do método?