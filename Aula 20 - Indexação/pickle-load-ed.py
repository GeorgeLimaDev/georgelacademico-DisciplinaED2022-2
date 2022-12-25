import pickle #Módulo para converter objetos em stream de bits e vice-versa.
import sys #Módulo para acessar arquivos em disco.

nomeArquivo = 'professores.bin'

try:
    arq = open(nomeArquivo, 'rb+')
    print(f'Arquivo {nomeArquivo} aberto com sucesso!')
except Exception as e:
    print(f'Erro na abertura do arquivo {nomeArquivo}. Informe o caminho correto.')
    print(e)
    sys.exit()

print('''
Byte Matricula Professor                      Disciplina
-=-= -=-=-=-=- -=-=-=-=-=-=-=-=-=-=-=-=-=-=-= -=-=-=-=-=-=-=-=-=-=-=-=-''')

arq.seek(0,0) #Posiciona a leitura no início do arquivo encontrado
posicao = arq.tell() #Obtém a posição de leitura
try:
    while True:
        mat, nome, disciplina = pickle.load(arq)
        print(f'{posicao:04d}   {mat:3d}    {nome:30s}  {disciplina}')
        posicao = arq.tell()

except EOFError:
    print('\nFim do arquivo encontrado.')
except Exception as e:
    print('Erro', e)
else:
    print('\nFim da leitura de dados.')

arq.close()