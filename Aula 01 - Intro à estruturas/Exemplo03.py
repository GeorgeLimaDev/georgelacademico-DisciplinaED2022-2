#Exemplo final substituindo a estrutura de decisão pelo tratamento de exceção:

URLS = {'www.ifpb.edu.br' : '1.1.1.1', 'uol.com.br' : '2.2.2.2', 'g1.com.br' : '3.3.3.3', 'www.george.com' : '4.4.4.4'}

while True:
    URL = input('Digite uma URL: ')
    URL = URL.lower()

    if len(URL) == 0:
        break
    #O tratamento de exceção vai tentar comparar a entrada com os valores do dicionário e tratar o erro 
    try:
        print(f'\tURL {URL} é válida. IP: {URLS[URL]}')
    except KeyError:
        print(f'\tURL {URL} não encontrada.')
    
    #Incluindo entradas no dicionário (apontando uma nova chave):
    URLS['www.joaopessoa.com'] = '5.5.5.5'
    #Alterando entradas no dicionário (referenciando uma chave já existente):
    URLS['www.ifpb.edu.br'] = '1.2.3.4'
    print(URLS)