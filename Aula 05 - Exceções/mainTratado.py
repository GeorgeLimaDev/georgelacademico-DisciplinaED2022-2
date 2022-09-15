notas = [7,8,9,10]

#OS comandos try e except indicam para o programa o que tentar primariamente, e caso as condições para funcionamento normal não sejam atendidas, ele busca acomodá-las em alguma das exceções indicadas e só aborta a execução caso nenhuma exceção consiga capturar o erro. Caso a captura ocorra é executado o bloco de código correspondente e a execução continua.
try:
    while True:
        index = int(input('Índice da nota desejada: '))

        if index < 0:
            break

        print('Nota: ', notas[index],'\n')

        #Esse teste foi criado somente para exemplificar a execução da exceção fileNotFoundError e o comando raise que "levanta" um indicativo de exceção.
        if index == 1:
            raise FileNotFoundError('Erro na abertura do arquivo.')

        print('Nota dividida pelo índice: ', notas[index]/index)

    print('Correto. Avançando para próxima iteração.')

#O comando as "..." permite capturar a mensagem interna da linguagem para o erro e exibi-la na tela junto à mensagem personalizada.
#ValueError faz com que somente números inteiros sejam aceitos no input.
except ValueError as ve:
    print('Indice inválido. Digite um número inteiro.')
    print('Mensagem embutida: ', ve)
#IndexError faz com que somente índices presentes na lista sejam aceitos.
except IndexError as ie:
    print(f'Erro: digite um número entre 0 e {len(notas)}.')
    print('Mensagem embutida: ', ie)
#ZeroDivisionError impede que o programa tente executar divisão por zero, matematicamente inaceitável.
except ZeroDivisionError as ze:
    print('Erro: a divisão não pode ser realizada com denominador zero.')
    print('Mensagem embutida: ', ze)
#BaseException captura interrupção da execução por comando de entrada (ctrl + D). Neste caso é necessário usar o detalhamento abaixo para que seja exibida corretamente.
except BaseException as be:
    print('Aconteceu algum problema. Reinicie.')
    print('Exceção responsável: ', be.__class__.__name__)
    print('Mensagem da exceção: ', be)

print('FIM DO PROGRAMA.')