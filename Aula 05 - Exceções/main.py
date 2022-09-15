#Programa de exemplo: uma lista de notas e uma entrada que seleciona o índice que é também o valor pelo qual ela será dividida.
#Nele as situações que podem quebra a execução do programa são tratadas com IFs, porém não é o ideal, por serem muitas para serem tratadas individualmente, tanto que o programa nem cobre todas as possibilidades de erro, como a entrada de texto no input.

notas = [7,8,9,10]

while True:
    #O valor digitado selecionará a nota e a dividirá por esse valor.
    index = int(input('Índice da nota desejada: '))

    if index < 0:
        break

    if index >= (len(notas)):
        continue

    print('Nota: ', notas[index], '\n')

    if index == 0:
        print('Não é possível dividir a nota por zero.')
    else:
        print('Nota dividida pelo índice: ', notas[index]/index)

print('FIM DO PROGRAMA.')