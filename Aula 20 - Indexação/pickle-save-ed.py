import pickle
import os

nomeArquivo = 'professores.bin'
arquivoEncontrado = os.path.isfile(nomeArquivo)

if arquivoEncontrado:
    arq = open(nomeArquivo, 'r+b')
    print(f'Arquivo {nomeArquivo} aberto com sucesso no modo r+b')
else:
    arq = open(nomeArquivo, 'w+b')
    print(f'Arquivo {nomeArquivo} NÃO ENCONTRADO. Criando um novo no modo w+b')


arq.seek(0,2)

dados = [(100, 'Alex', 'ED'), (101, 'Cândido', 'APE'), (110, 'Luiz', 'HTML'),\
(141, 'Damires', 'BD II'), (151, 'Alana', 'Padrões de projeto'),\
(168, 'Leônidas', 'Arq. de Computadores'), (181, 'Fausto', 'POO'), (132, 'Márcio', 'Intr. Redes'), (111, 'Petronio', 'IHC')]

if arquivoEncontrado:
    print('Adicione mais dados ao arquivo existente.')
    while True:
        mat = int(input('Matrícula: (Digite 0 para encerrar): '))
        if mat == 0:
            break
        nome = input('Nome do professor: ')
        disciplina = input('Disciplina: ')
else:
    print('Criando arquivo binário de dados...')
    progresso = 0
    for registro in dados:
        pickle.dump(registro, arq)
        progresso += 1
        print(f'{progresso} registro {registro[1]} salvo.')
    print('Fim da geração do arquivo.')

arq.close()