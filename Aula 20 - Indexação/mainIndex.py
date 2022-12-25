import os #Para verificar a existência do arquivo solicitado.
import sys #Para uso da função exit.
import pickle #Para manipular arquivos binários.

def loadData(nomeArquivo):
    try:
        print(f'(1) Abrindo arquivo binário {nomeArquivo}...')
        arq = open(nomeArquivo, 'rb+')
        print(f'Arquivo aberto com sucesso.')

        index = None #Corresponde ao dicionário de indexação.
        indexFile = nomeArquivo.split('.')[0] + '.idx' #Formata o argumento em um formato em que pode ser testado se ele já existe no diretório selecionado.

        if not os.path.isfile(indexFile):
            print(f'(2) CRIANDO arquivo de índice {indexFile}...')
            index = createIndex(arq, indexFile)
        else:
            print(f'(2) CARREGANDO arquivo de índice {indexFile}...')
            index = loadIndex(indexFile)
    
    except Exception as e:
        print(e)
        print(f'Erro na abertura do arquivo {nomeArquivo}. Informe o caminho correto.')
        sys.exit()
    finally:
        arq.close()
    
    return index

def createIndex(mainFile, indexFile):

    docentes = {}

    try:
        arqidx = open(indexFile, 'w+b')
        try: #Montando a estrutura de índice em memória
            mainFile.seek(0,0) #Posiciona a leitura no início.
            posicao = mainFile.tell() #Obtendo o endereço para início da leitura.
            print('Povoamento da estrutura de índice em memória...')
            while True:
                mat, nome, disciplina = pickle.load(mainFile) #Lendo um registro por vez.
                docentes[mat] = posicao
                print(f'\tmatrícula={mat:3d},posicao={posicao:04d}')
                posicao = mainFile.tell()
        except EOFError: #Sinaliza o fim da escrita do arquivo.
            print('Fim da construção da estrutura de índice em memória.')
            pass
        except Exception as e:
            print('createIndex(): ',e)

        print('   ',docentes)
        print('Criando o arquivo de índice no disco a partir das tuplas (matrícula, byte)...') #Salvando a estrutura de índices criada.
        for k in sorted(docentes.keys()):
            print(f'({k},{docentes[k]})')
            pickle.dump((k,docentes[k]), arqidx)
        
    except Exception as e:
        raise Exception(f'Erro na criação do arquivo de índice {indexFile}.')
    else:
        print('Operação concluída com sucesso.')
    finally:
        arqidx.close()
    
    return docentes

def loadIndex(indexFile):
    docentes = {}

    try:
        arqidx = open(indexFile, 'r+b')
        print('Povoamento da estrutura de índice em memória...') #Montando a estrutura de índices para exibição.
        while True:
            mat, posicao = pickle.load(arqidx) #Lendo um registro por vez.
            docentes[mat] = posicao
            print(f'\tMatrícula={mat:3d},posicao={posicao:04d}')
            posicao = arqidx.tell() #informa o próximo docente para leitura.
    except EOFError: #Sinaliza o fim da leitura do arquivo.
        pass
    finally:
        arqidx.close()
    print('Operação concluída com sucesso.')
    return docentes


#Programa principal para testes:

nomeArquivo = 'professores.bin'
index = loadData(nomeArquivo)
print()
print('Programa principal')
print('Estrutura de indexação carregada:')
print(index)
