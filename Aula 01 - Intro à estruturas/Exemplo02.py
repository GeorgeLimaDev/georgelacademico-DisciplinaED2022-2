#Modificando o programa anterior para usar um dicionário ao invés das duas listas.

#O dicionário combina os dados das duas listas anteriores no formato de chave e valor associando cada URL a um IP.
URLS = {'www.ifpb.edu.br' : '1.1.1.1', 'uol.com.br' : '2.2.2.2', 'g1.com.br' : '3.3.3.3', 'www.george.com' : '4.4.4.4'}

while True:
    URL = input('Digite uma URL: ')
    URL = URL.lower()

    if (len(URL) == 0):
        break

    if URL in URLS.keys():
        print(f'\tURL {URL} é válida. IP: {URLS[URL]}')
    else:
        print(f'\tURL {URL} não encontrada.')

    #print(URLS)
    #É possível incluir novos elementos no dicionário:
    URLS['www.joaopessoa.com'] = '5.5.5.5'
    #Também é possível alterar elementos especificando a chave dele:
    URLS['www.ifpb.edu.br'] = '1.2.3.4'
    print(URLS)