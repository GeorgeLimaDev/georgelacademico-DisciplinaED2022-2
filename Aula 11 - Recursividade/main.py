#Forma comum de estrutura de repetição:
def potenciaIterativa (base, expoente):
    resultado = 1
    for i in range (expoente):
        resultado *= base
    return resultado

#Definição de recursividade: uma função que dentro de seu escopo chama a si mesma, resultando em um laço.
#Forma recursiva:
def potenciaRecursiva (base, expoente, contador) -> int:
    #Gerando um contador para acompanhar as mudanças a cada chamada.
    print(f'chamada {contador}: Base: {base}, Expoente: {expoente}')
    if expoente == 0:
        return 1
        #Tratamento do caso base: foge da regra matemática geral para o problema, por isso deve ser separado.
    else:
        return base * potenciaRecursiva(base, expoente - 1, contador + 1)
        #Lógica: mantém o valor da base e vai multiplicando ele pelo expoente por um valor menor a cada iteração. Quando o expoente for 0 a chamada volta ao início e os valores acumulados são devolvidos para cada chamada até chegar na primeira.

#Exercício: foi pedido para interpretar a função e prever o valor que ela retornaria.
def frec (i, j)->int:
    if i == j:
        return 0
    else:
        return i + frec(i+1, j)

#Exercício 2: mesma proposta do anterior.
def printNumbers(n):
    if n == 0:
        return
    print(n, end=' ')
    printNumbers(n-1)

#Comparando os resultados com os dois métodos:
print(potenciaIterativa(2,3))
print(potenciaRecursiva(2,3,0))

#Conferindo os exercícios:
print(frec(2,6))
print(printNumbers(10))