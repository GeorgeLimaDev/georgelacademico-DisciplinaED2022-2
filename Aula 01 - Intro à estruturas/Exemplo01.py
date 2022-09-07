#Conteúdo da primeira aula da disciplina: explorando as diferenças entre o modelo estruturado básico e com uso de estruturas mais complexas, como o dicionário.

#Apenas com programação estruturada:
#Este código compara a entrada do usuário com as URLs já presentes na lista. Caso a entrada coincida com um dos elementos é retornado o IP daquele site.
urls = ['www.ifpb.edu.br', 'uol.com.br', 'www.g1.com.br', 'www.alex.com']
ips = ['1.1.1.1', '2.2.2.2', '3.3.3.3', '4.4.4.4']

while True:
    url = input('Digite uma URL: ')

    if len(url) == 0:
        break #Para o programa caso a entrada seja vazia.

    achou = False
    for i in range (len(urls)):
        if (urls[i] == url):
            print(f'\tURL válida. IP {ips[i]}')
            achou = True
            break
    if not achou:
        print(f'\tURL {url} não encontrada.')
